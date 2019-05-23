from pathlib import Path
import os

os.chdir('data/thucnews')

folder_name_list = ['体育', '财经', '房产', '家居', '教育', '科技', '时尚', '时政', '游戏', '娱乐']

for fn in folder_name_list:
	Path(fn).mkdir(parents=True, exist_ok=True)
