# ----------------------------------------
# @file thumbnail.py
# @breif 複数画像からサムネイル(1ファイル)とファイルリストを作成
# @author OCHIAI Takeshi
# makeThumbnail
# @date 2019/02/02
# ----------------------------------------

import os.path
import PIL.Image
import glob

if __name__ == '__main__':
    pathlist = []
    # 対象画像のpathを取得(orgディレクトリ決め打ち)
    for path in glob.glob('./org/*.jpg'):
        pathlist.append(path)
    # ファイルの個数から、出力サイズを取得
    out_width  = 100 * 10
    out_height = 100 * (len(pathlist) // 10 + 1)
    # 出力ファイル名も決め打ち
    out_filename = './thumb.jpg'
    # 出力画像のベースを生成
    out_img    = PIL.Image.new('RGB', (out_width, out_height), (10, 10, 10))
    # ファイル名出力用ファイルを用意
    with open('filename.csv', 'w') as fw:
        for i, path in enumerate(pathlist):
            # ファイルリストを出力
            fw.write(os.path.basename(path) + '\n')
            # 画像をオープン
            img = PIL.Image.open(path)
            x = img.size[0]
            y = img.size[1]
            if x < y:
                thumb_y = 100
                thumb_x = int(100 / (y / x))
            else:
                thumb_x = 100
                thumb_y = int(100 / (x / y))
            # 画像を縮小して貼り付け
            thumb_img = img.resize((thumb_x, thumb_y))
            out_img.paste(thumb_img, ((i % 10) * 100, (i // 10) * 100))
    out_img.save(out_filename, quality = 95)
