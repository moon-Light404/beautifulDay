menu ={
      "福建":{
          "福州":{
              "闽侯":{},
              "连江":{},
              "马尾":{}
          },
          "厦门": {
              "思明":{},
             "湖里": {},
             "集美": {}
         },
         "泉州": {
             "丰泽":{},
             "洛江": {},
             "泉港": {}
         },

     },
     "上海":{
         "浦东":{
             "陆家嘴":{},
             "张江":{},
             "川沙":{}
         },
         "静安": {
             "静安寺":{},
             "南京西路":{}
         },
         "宝山": {
             "吴淞街道":{},
             "友谊街道": {},
             "张庙街道": {}
         },

     },
     "广东":{
         "广州":{
             "白云区":{},
             "海珠区": {},
             "越秀区": {}

         },
         "深圳": {
             "南山区": {},
             "罗湖区": {},
             "宝安区": {}
         },
         "汕头": {
             "潮阳区": {},
             "潮安区": {},
             "澄海区": {}
         },

     }
 }
current_layer = menu
parent_layer = []
flags = False
while not flags:
  for key in current_layer:
   print(key)
  choice = input("请输入相应的名称(退出输入q，返回上一层输入b)").strip()#strip()用于移除字符串头尾指定的字符
  #（默认位空格或换行符）
  if choice in current_layer:
   parent_layer.append(current_layer)
   current_layer = current_layer[choice]
  elif choice == 'b':
   if parent_layer:
    current_layer = parent_layer.pop()#pop()返回列表中最后一个菜单，也就是上一级菜单
  elif choice == 'q':
   flags = True
  else:
   print("查无此人")


