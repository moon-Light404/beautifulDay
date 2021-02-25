PETS = []
import pickle
#--------------------------------------------
flag = True
try:
	f = open('pet.txt','rb')
	PETS = pickle.load(f)
	print(PETS)
	f.close()
except:
	pet = {'id':'1001','name':'小火苗','category':'火系','price':15}
	PETS.append(pet)
	f = open('pet.txt','wb')
	pickle.dump(PETS,f)
	f.close()
#------------------------------------------
def add_pet():
	ID = input("请输入宠物编号：")
	for i in PETS:
		if ID == i['id']:
			print('该宠物已经添加过了，请输入新的宠物!')
			break
	else:
		name = input("请输入宠物名称：")
		category = input("请输入宠物种类:")
		price = input("请输入宠物价格：")
		pet = {'id':ID,'name':name,'category':category,'price':price}
		PETS.append(pet)
		print("恭喜宠物添加成功！")

def search_pet():
	name = input("请输入宠物名称：")
	for pet in PETS:
		if pet['name'] == name:
			text = "编号：{},名称:{},种类:{},价格:{}".format(
				pet['id'],
				pet['name'],
				pet["category"],
				pet['price']
				)
			print(text)

def delete_pet():
	ID = input("请输入宠物编号：")
	for pet in PETS:
		if pet['id'] == ID:
			PETS.remove(pet)
			print("删除宠物成功！")
			break

def list_pet():
	for pet in PETS:
		text = "编号：{},名称:{},种类:{},价格:{}".format(
				pet['id'],
				pet['name'],
				pet["category"],
				pet['price']
				)
		print(text)
def save0bj():
	f = open('pet.txt','wb')
	pickle.dump(PETS,f)
	f.close()
	print('保存信息成功!')



#--------------------------------------------


def main():
	print('='*30)
	print('1.添加宠物')
	print('2.查找宠物')
	print('3.删除宠物')
	print('4.列出宠物')
	print('5.保存信息')
	print('6.退出系统')
	print('='*30)

	while True:
		option = input("请输入选项：")
		if option == '1':
			add_pet()
		elif option == '2':
			search_pet()
		elif option == '3':
			delete_pet()
		elif option == '4':
			list_pet()
		elif option == '5':
			save0bj()
		elif option == '6':
			print('再见，欢迎下次使用!')
			exit()

		else:
			print("请输入正确的选项")
main()