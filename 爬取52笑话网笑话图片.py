import requests
import re
import os

if __name__ == '__main__':

    save_dir = './xiaohua_picture'

    if not os.path.exists('./xiaohua_picture'):
        os.mkdir(save_dir)
        print("success")

    url = 'https://www.52xiaohua.com/category-3_%d.html'

    for num in range(1,6):

        current_url = url % num

        page_text = requests.get(url=current_url).text

        ex = '<ul class="postthumb".*?<img src="(.*?)"'

        img_src_list = re.findall(ex,page_text,re.S)

        print(img_src_list)

        for src in img_src_list:

            img_text = requests.get(url=src).content

            img_name = src.split('/')[-1]

            save_path = os.path.join(save_dir,img_name)

            with open(save_path,'wb') as fp:
                fp.write(img_text)
                print(img_name," success!")
