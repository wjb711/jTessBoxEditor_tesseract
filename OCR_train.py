

import os

comments='''
tesseract的自制字体识别的简化操作流程
先要把tesseract路径加入到系统path
本脚本用于简化文字识别的程序，配合jTessBoxEditor使用，需要先下载
参考操作指南
http://www.cnblogs.com/zhongtang/p/5555950.html
第一步，先完成准备样本图片，存成tiff格式，所有字必须在一行，不能多行，换行
第二步，合并样本图片：
打开jtessboxeditor，点击Tools->Merge Tiff ，按住shift键选择前文提到的101个tif文件，并把生成的tif合并到新目录d:\python\lnypcg\new下，命名为langyp.fontyp.exp0.tif
第三步
执行命令生成langyp.fontyp.exp0.box文件

tesseract langyp.fontyp.exp0.tif langyp.fontyp.exp0 -l eng -psm 7 batch.nochop makebox
第四步
切换到jTessBoxEditor工具的Box Editor页，点击open，打开前面的tiff文件langyp.fontyp.exp0.tif，工具会自动加载对应的box文件。

检查box数据，如下图所示，数字8被误认成字母H，手工修改H成8，并保存。

点击下图红色框的按钮，逐个核对tif文件的box数据，全部检查结束并保存。
如不能保存，先添加再删除即可保存
第五步起，可通过脚本完成
'''
print (comments)
create_box=input('如需要手动生成langyp.fontyp.exp0.box文件，按y键，否则任意键继续：')
if create_box=='y':
    os.system('tesseract langyp.fontyp.exp0.tif langyp.fontyp.exp0 -l eng -psm 7 batch.nochop makebox')
print ('第五步生成font_properties')

os.system('echo fontyp 0 0 0 0 0 >font_properties')
print ('第六步生成训练文件')
os.system('tesseract langyp.fontyp.exp0.tif langyp.fontyp.exp0 -l eng -psm 7 nobatch box.train')

print ('第七步生成字符集文件')
os.system('unicharset_extractor langyp.fontyp.exp0.box')

print ('第八步生成shape文件')
os.system('shapeclustering -F font_properties -U unicharset -O langyp.unicharset langyp.fontyp.exp0.tr')

print ('第九步生成聚集字符特征文件')
os.system('mftraining -F font_properties -U unicharset -O langyp.unicharset langyp.fontyp.exp0.tr')

print ('第十步生成字符正常化特征文件')
os.system('cntraining langyp.fontyp.exp0.tr')


print ('第十一步更名')
os.system('rename normproto fontyp.normproto')
os.system('rename inttemp fontyp.inttemp')
os.system('rename pffmtable fontyp.pffmtable')
os.system('rename unicharset fontyp.unicharset')
os.system('rename shapetable fontyp.shapetable')

print ('第十二步合并训练文件')
os.system('combine_tessdata fontyp.')

input('结束， 任意键退出')
