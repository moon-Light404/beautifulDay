package day4;

import java.util.*;
import java.io.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.regex.Pattern;//正则表达式

class recitePanel extends JTabbedPane implements ActionListener {
    //第一个面板
    JPanel jp1;
    JButton  jb1, jb2, jblast,jbnext, jb4, jb5, jb_clear, jb6;
    //  jb1不认识   jb2认识  jb3下一个  jb4存档 jb5删除 jb_clear 清空 jb6收藏
    // jblast 上一个 jbnext 下一个
    JComboBox<String> lib;// 文件单选框
    String[] b1 = new String[]{"无","四级","六级","我的生词本","字典"}; // 单选框内容
    JButton jb_reopen;// 重新开始



    JLabel  smalllable;//标签2个
    //2个面板
    JTextField jtf1, jtf2, jtf3;// 3个文本框
    // jtf1显示英文 jtf2显示中文 jtf3显示上一个单词
    JTextField addchange_Eng,addchange_chi;//  add_Eng添加英文  add_chi添加中文
    JButton add_confirm;// 确认添加到文件中
    JLabel first_1,first_2;// 中文和英文提醒标签



    //  重要的变量声明和定义
    Dictionary dictionary;//字典集合声明声明声明
    Map<String,String> mywords = new HashMap<String,String>();
    //   记录我的生词本中的单词
    ArrayList<Integer> mylist = new ArrayList<Integer>();//   存储随机数
    String tempkey;//  临时存储当前选中的单词的key
    Random random = new Random();
    int index;//   随机数
    maptools first_tool = new maptools();// 工具类


    //  第二个面板
    JPanel jp2;
    JTextField jtf4,jtf5;//  jtf4自测英文  jtf5自测输入中文
    JButton jb_confirm,jb_restart,jb_master,jb_save;
    //确认按钮  重开按钮  已掌握  保存
    JButton jb_check;
    //查询单词表按钮

    //  第三个面板
    JPanel jp3;
    JTextField jt1,jt2;// 添加单词到我的生词本中
    JButton bu_add;// 添加单词按钮
    JLabel l1,l2;// 两个标签表示中文英文




    int i;
    Boolean flag=false;

    String filepath;// 作文件全局变量记录打开的文件路径信息

    recitePanel() {
        this.Component();
        this.reader(); //初始化Map我的单词表
        jp1.add(jtf1);
        jp1.add(jtf2);
        jp1.add(jb6);//收藏单词到单词本
        jp1.add(jtf3);
        jp1.add(lib);
        jp1.add(jb1);
        jp1.add(jb2);
        jp1.add(jblast);
        jp1.add(jbnext);
        jp1.add(jb4);
        jp1.add(jb5);
        jp1.add(jb_clear);
        jp1.add(jb_reopen);
        jp1.add(first_1);// 英文
        jp1.add(addchange_Eng);
        jp1.add(first_2);  //中文
        jp1.add(addchange_chi);
        jp1.add(add_confirm);


        jp2.add(jtf4);
        jp2.add(jtf5);
        jp2.add(jb_confirm);//确认按钮
        jp2.add(jb_restart);
        jp2.add(jb_master);
        jp2.add(jb_save);
        jp2.add(jb_check);

        jp3.add(l1);
        jp3.add(jt1);
        jp3.add(l2);
        jp3.add(jt2);
        jp3.add(bu_add);


        this.add(jp1, "简单");
        this.add(jp2,"单词测试(生词本)");
        this.add(jp3,"添加到生词本");

        lib.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                int index = lib.getSelectedIndex();
                switch (index){
                    case  0:
                        flag = false;
                        i = 0;
                        mylist.clear();
                        jtf1.setText(null);
                        jtf2.setText(null);
                        break;
                    case 1:
                        i = 0;
                        mylist.clear();
                        dictionary = new Dictionary("file/四级.txt");
                        dictionary.addWords("file/四级.txt");
                        if(dictionary.words.size()!=0 ) {// 防止文件为空
                            flag = true;// 只有文件有单词才可以置为true
                            jtf1.setText(dictionary.words.get(0).word);
                            jtf2.setText(null);
                        }
                        break;
                    case 2:
                        flag = true;
                        i = 0;// 初始化使得从第一个单词开始
                        mylist.clear();
                        dictionary = new Dictionary("file/六级.txt");
                        dictionary.addWords("file/六级.txt");
                        if(dictionary.words.size()!=0 ){
                            jtf1.setText(dictionary.words.get(0).word);
                            jtf2.setText(null);
                        }
                        break;
                    case 3:
                        flag = true;
                        i = 0;// 初始化使得从第一个单词开始
                        mylist.clear();
                        dictionary = new Dictionary("file/我的生词本.txt");
                        dictionary.addWords("file/我的生词本.txt");
                        if(dictionary.words.size()!=0 ){
                            jtf1.setText(dictionary.words.get(0).word);
                            jtf2.setText(null);
                        }
                        break;
                    case 4:
                        flag = true;
                        i = 0;// 初始化使得从第一个单词开始
                        mylist.clear();
                        dictionary = new Dictionary("file/Allwords.txt");
                        dictionary.addWords("file/Allwords.txt");
                        if(dictionary.words.size()!=0 ){
                            jtf1.setText(dictionary.words.get(0).word);
                            jtf2.setText(null);
                        }
                        break;
                    default:
                        break;
                }
            }
        });
    }




    public void reader(){
        Scanner input2 = null;
        try{
            input2 = new Scanner(new File("file/我的生词本.txt"),"utf-8");
            while(input2.hasNext()){//如果没有就不会进行下面的赋值
                mywords.put(input2.next(),input2.next());
            }
        }catch (FileNotFoundException e3){
            e3.printStackTrace();
        }finally {
            input2.close();
        }
        if(!mywords.isEmpty()){//只有文件不空时散列表才有数据，才能取出单词信息
            Randomords(); // 这里不能套用maptool中的函数，因为这里要判断是否需要再产生一个单词
        }
    }


    public void Component()    //创建组件的函数
    {

        i = 0;//第一个单词开始
        smalllable = new JLabel();
        smalllable.setText("刚刚");
        smalllable.setForeground(Color.green);

        lib = new JComboBox<String>(b1);
        lib.setBounds(480,50,100,30);

        jb1 = new JButton("不认识");
        jb1.setBounds(30,85,130,50);
        jb1.addActionListener(this);
        jb1.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR)); //设置鼠标放上去变为小手
        jb1.setIcon(new ImageIcon("image/angry.png"));    //按钮上添加图片
        jb2 = new JButton("认识");
        jb2.setBounds(165,85,125,50);
        jb2.addActionListener(this);
        jb2.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        jb2.setIcon(new ImageIcon("image/happy.png"));

        jblast = new JButton("上一个");
        jblast.setBounds(310,95,80,40);
        jblast.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        jblast.addActionListener(this);

        jbnext = new JButton("下一个");
        jbnext.setBounds(400,95,80,40);
        jbnext.addActionListener(this);
        jbnext.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));

        jb4 = new JButton("存档");
        jb4.setBounds(30,140,130,50);
        jb4.addActionListener(this);
        jb4.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        jb4.setIcon(new ImageIcon("image/保存.png"));

        jb5 = new JButton("删除");
        jb5.setBounds(165,140,130,50);
        jb5.addActionListener(this);
        jb5.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        jb5.setIcon(new ImageIcon("image/删除.png"));

        jb_clear = new JButton("清空");//清空前面两个文本框
        jb_clear.setBounds(315,140,130,50);
        jb_clear.addActionListener(this);
        jb_clear.setIcon(new ImageIcon("image/清空.png"));


        jb6 = new JButton("收藏");
        jb6.setBounds(470,5,70,30);
        jb6.addActionListener(this);
        jb6.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        jb6.setBackground(Color.GREEN);

        jb_reopen = new JButton("重新学习");
        jb_reopen.setBounds(465,145,130,35);
        jb_reopen.setBackground(Color.BLUE);
        jb_reopen.addActionListener(this);

        add_confirm = new JButton("添加到此单词表");
        add_confirm.setBounds(150,300,150,50);
        add_confirm.addActionListener(this);

        jp1 = new JPanel();
        jp1.setLayout(null);

        jp2 = new JPanel();
        jp2.setLayout(null);

        jp3 = new JPanel();
        jp3.setLayout(null);



        jtf1 = new JTextField("Engilsh",18);//设置文本域宽度
        jtf1.setEditable(false);    //设置文本不可编辑
        jtf1.setFont(new Font("黑体", Font.PLAIN, 20));    //设置文本字体
        jtf1.setBounds(20,5,200,30);

        //jtf1.setText(dictionary.words.get(0).word);		//设置文本域初始值

        jtf2 = new JTextField("Chinese",18);    //设置文本域宽度
        jtf2.setEditable(false);
        jtf2.setFont(new Font("黑体", Font.PLAIN, 20));
        jtf2.setBounds(260,5,200,30);

        jtf3 = new JTextField(30);
        jtf3.setBounds(30,45,400,30);
        jtf3.setEnabled(false);
        jtf3.setFont(new Font("黑体", Font.PLAIN, 20));

        addchange_Eng = new JTextField(20);
        addchange_Eng.setBounds(265,220,250,30);
        addchange_Eng.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        addchange_chi = new JTextField(15);
        addchange_chi.setBounds(80,260,300,30);
        addchange_chi.setFont(new Font("黑体", Font.PLAIN, 18));

        first_1 = new JLabel("请输入你想添加的单词 英文:");
        first_1.setFont(new Font("黑体", Font.PLAIN, 17));
        first_1.setBounds(20,220,250,20);

        first_2 = new JLabel("中文");
        first_2.setBounds(30,260,40,20);
        first_2.setFont(new Font("黑体", Font.PLAIN, 17));

        jtf4 = new JTextField(18);
        jtf4.setBounds(20,5,200,30);
        jtf4.setFont(new Font("黑体", Font.PLAIN, 20));

        jtf5 = new JTextField("输入中文",18);
        jtf5.setBounds(225,5,200,30);
        jtf5.setFont(new Font("黑体", Font.PLAIN, 20));


        l1 = new JLabel("英文");
        l1.setBounds(20,5,40,30);
        l1.setFont(new Font("黑体", Font.PLAIN, 17));
        l2 = new JLabel("中文");
        l2.setBounds(20,40,40,30);
        l2.setFont(new Font("黑体", Font.PLAIN, 17));


        jt1 = new JTextField(12);
        jt1.setBounds(65,5,250,30);
        jt1.setFont(new Font("黑体", Font.PLAIN, 20));

        jt2 = new JTextField(12);
        jt2.setBounds(65,40,250,30);
        jt2.setFont(new Font("黑体", Font.PLAIN, 20));

        bu_add = new JButton("添加单词");
        bu_add.setBounds(65,100,120,30);




        jb_confirm = new JButton("确认");
        jb_confirm.setBounds(450,5,80,30);
        jb_confirm.addActionListener(this);

        jb_restart = new JButton("重新测试");
        jb_restart.setBounds(25,55,100,30);
        jb_restart.addActionListener(this);

        jb_master = new JButton("已掌握");
        jb_master.setBounds(130,55,80,30);
        jb_master.addActionListener(this);

        jb_check = new JButton("查看生词表");
        jb_check.setBounds(320,55,100,30);
        jb_check.addActionListener(this);

        jb_save = new JButton("确认删除");
        jb_save.setBounds(215,55,100,30);
        jb_save.addActionListener(this);


        bu_add.addActionListener(this);

    }


    @Override
    public void actionPerformed(ActionEvent e) {
        // TODO Auto-generated method stub
        if (e.getSource() == jb1 && flag)        //点击第一个按钮
        {
            jtf2.setText(dictionary.words.get(i).character);    //显示单词解释
        }
        else if (e.getSource() == jb2 && flag)    //点击第二个按钮
        {
            jtf3.setText( dictionary.words.get(i).word + "\t" + dictionary.words.get(i).character);
//
        }
        else if(e.getSource() == jblast && flag) {
            if (i > 0) {
                this.i--;
                jtf3.setText(null);
                jtf1.setText(dictionary.words.get(i).word);
                jtf2.setText(null);
                jtf3.setText( "刚刚"+dictionary.words.get(i+1).word + "\t" + dictionary.words.get(i+1).character);

                
            } else {
                JOptionPane.showMessageDialog(this, "这是第一个单词", null, JOptionPane.INFORMATION_MESSAGE);
                jtf2.setText(null);
            }
        }
        else if (e.getSource() == jbnext && flag) //如果点击第三个按钮
        {
            if (i < dictionary.words.size()-1 )  //如果最后一个单词
            {
                this.i++;    //单词序号加1
                jtf1.setText(dictionary.words.get(i).word);    //显示下一个单词的英文
                jtf2.setText(null);        //清空单词解释
                jtf3.setText( "刚刚 :"+dictionary.words.get(i-1).word + "\t" + dictionary.words.get(i-1).character);
            } else    //如果是最后一个单词
            {

                JOptionPane.showMessageDialog(this,"最后一个单词了",null,JOptionPane.INFORMATION_MESSAGE);
                jtf2.setText(null);        //清空单词解释
            }
        }
        else if (e.getSource() == jb4 && flag)    //如果点击第四个按钮
        {
            dictionary.saveWords();
            jtf2.setText("进度保存成功");        //清空单词解释
        }
        else if (e.getSource() == jb5 && flag) {
            if (i < dictionary.words.size()-1) {
                dictionary.words.remove(i);        //从集合中移除该单词
                jtf1.setText(dictionary.words.get(i).word);    //显示下一个单词的英文
                jtf2.setText(null);        //清空单词解释
            } else {
                dictionary.words.remove(i);// 当轮到最后一个单词就不用显示下一个单词了
                jtf1.setText("最后一个单词了");  //单词库尽
                jtf2.setText(null);        //清空单词解释
            }
        }
        else if (e.getSource() == jb_clear && flag) {
            jtf1.setText(null);
            jtf2.setText(null);
            jtf3.setText(null);
        }
        else if (e.getSource() == jb6 && flag) {
            if(first_tool.CollectWords(mywords,dictionary.words.get(i).word, dictionary.words.get(i).character,"file/我的生词本.txt")){
                JOptionPane.showMessageDialog(this,"收藏成功",null,JOptionPane.INFORMATION_MESSAGE);
            }
            else{
                JOptionPane.showMessageDialog(this,"已经收录该单词",null,JOptionPane.INFORMATION_MESSAGE);
            }

        }
        else if(e.getSource() == jb_reopen && flag ){//  要确认已经选择打开了文件
            i = 0;//  让i从0开始
            jtf1.setText(dictionary.words.get(0).word);
            jtf2.setText(null);
        }
        else if(e.getSource() == add_confirm ){
            if(flag){
                if(!isContain(addchange_Eng.getText())){//不包含在里面
                    if(first_tool.isEng(addchange_Eng.getText()) && first_tool.isChi(addchange_chi.getText())) {//  判断中英文格式
                        Word word = new Word();
                        word.word = addchange_Eng.getText();
                        word.character = addchange_chi.getText();
                        dictionary.words.add(word);
                        first_tool.savetoFile(addchange_Eng.getText(), addchange_chi.getText(), dictionary.filename); //  加入到当前操作的文件中去
                        JOptionPane.showMessageDialog(this,"添加成功",null,JOptionPane.INFORMATION_MESSAGE);
                        addchange_Eng.setText(null);
                        addchange_chi.setText(null);
                    }
                    else{
                        JOptionPane.showMessageDialog(this,"请输入正确的格式",null,JOptionPane.INFORMATION_MESSAGE);
                        addchange_Eng.setText(null);
                        addchange_chi.setText(null);
                    }
                }
                else{
                    JOptionPane.showMessageDialog(this,"已经收录该单词",null,JOptionPane.INFORMATION_MESSAGE);
                    addchange_Eng.setText(null);
                    addchange_chi.setText(null);
                }
            }
            else{  //  还没有选择文件
                JOptionPane.showMessageDialog(this,"还没有打开任何文件",null,JOptionPane.INFORMATION_MESSAGE);
            }
        }
        else if(e.getSource() == jb_confirm ){//确认按钮
            if(jtf5.getText().equals(mywords.get(tempkey))){
                    JOptionPane.showMessageDialog(this,"回答正确",null,JOptionPane.INFORMATION_MESSAGE);
                //回答正确提示框
                Randomords();//下一个随机单词
                jtf5.setText(null);
            }
            else{
                JOptionPane.showMessageDialog(this,"回答错误",null,JOptionPane.INFORMATION_MESSAGE);
                //回答错误提示框
            }
        }
        else if(e.getSource() == jb_restart ){//重新开始
            mylist.clear(); //重新开始清空两个表
            mywords.clear();
            reader();//  再从文件中读取单词到mywords里面
            if(!mywords.isEmpty()) {
//               Randomords();
            }//    清空随机数记录,从新开始测试单词
            else{
                JOptionPane.showMessageDialog(this, "没有单词", null, JOptionPane.INFORMATION_MESSAGE);
            }

        }
        else if(e.getSource() == jb_master ){//   掌握了就删除该单词
            if(mywords.keySet().size()>1) {
                mywords.keySet().removeIf(key -> key == tempkey);//删除该单词
                mylist.remove(mylist.size()-1);//删除链表最后一个元素
                JOptionPane.showMessageDialog(this, "删除成功,点击确认保存", null, JOptionPane.INFORMATION_MESSAGE);
                Randomords();
            }else{//只有一个单词
                mywords.keySet().removeIf(key -> key == tempkey);
                jtf4.setText(null);
                JOptionPane.showMessageDialog(this, "删除成功,已经没有单词了", null, JOptionPane.INFORMATION_MESSAGE);
            }
        }
        else if(e.getSource() == jb_save ){
            first_tool.saveMaptoFile(mywords,"file/我的生词本.txt");//  保存到文件中
            JOptionPane.showMessageDialog(this,"保存成功",null,JOptionPane.INFORMATION_MESSAGE);
        }
        else if(e.getSource() == bu_add){
            if(jt1.getText().equals("") || jt2.getText().equals("")){
                JOptionPane.showMessageDialog(this,"输入的信息不全",null,JOptionPane.INFORMATION_MESSAGE);
            }
            else {
                if(first_tool.isEng(jt1.getText()) && first_tool.isChi(jt2.getText())) {
                    if( first_tool.CollectWords(mywords,jt1.getText(), jt2.getText(),"file/我的生词本.txt")){//将文本框对应的单词对加进文件
                        JOptionPane.showMessageDialog(this, "收藏成功", null, JOptionPane.INFORMATION_MESSAGE);
                        jt1.setText(null);
                        jt2.setText(null);
                    }else{
                        JOptionPane.showMessageDialog(this, "已经收录该单词", null, JOptionPane.INFORMATION_MESSAGE);
                    }

                }
                else{
                    JOptionPane.showMessageDialog(this,"左边是英文 右边是中文哦 请输入正确的格式",null,JOptionPane.INFORMATION_MESSAGE);
                }
            }
        }
        else if(e.getSource() == jb_check){
            JTableDe dic = new JTableDe();
            dic.createComponent("file/我的生词本.txt");

        }

    }

    //  判断在文件中是否包含该英文
    public Boolean isContain(String wd){
        for(Word temp: dictionary.words){ // 遍历words数组查找是否重复
           if(temp.word.equals(addchange_Eng.getText())){// 找到是否有相同的英文
               return true;
           }
        }
        return false;  // 没有这个英文单词
    }

//
//    //   收藏单词到生词本中去,添加到mywords中
//    public Boolean CollectWords(String key,String value,String fileName) {
//        if(!mywords.containsKey(key)) {
//            //   myword中不包含这个键(单词),则添加到文件
//            mywords.put(key,value);//   先把单词信息添加到mywords中
//
//            first_tool.savetoFile(key,value,fileName);//  保存到文件
//            JOptionPane.showMessageDialog(this, "收藏成功", null, JOptionPane.INFORMATION_MESSAGE);
//            return true;// 收藏成功
//        }
//        else{//如果单词重复了
//            JOptionPane.showMessageDialog(this,"已经收录该单词",null,JOptionPane.INFORMATION_MESSAGE);
//            //提示已经收录，无需再次添加
//            return false;// 收藏失败
//        }
//    }



//    public void savetoFile(String key,String value,String fileName){//  把单词保存到任意文件
//        try {
//            FileWriter writer = new FileWriter(fileName, true);
//            writer.write(" "+ key+ " " + value + " ");
//            // 把单词加到生词本当中去
//            writer.close();
//
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//    }




    public void Randomords(){
        String [] keys = mywords.keySet().toArray(new String[0]);
        index = random.nextInt(keys.length);

        if(mylist.size()<keys.length) {//防止随机出现的单词重复
            while (mylist.contains(index)) {//包含了它
                index = random.nextInt(keys.length);
            }
            mylist.add(index);//添加索引到链表中
            String randomKey = keys[index];
            tempkey = randomKey;
            jtf4.setText(randomKey);//显示文本
        }
        else{
            JOptionPane.showMessageDialog(this,"你已经全部答对了",null,JOptionPane.INFORMATION_MESSAGE);
        }
    }

//    public void saveMyWords()		// 保存单词进度函数,保存到我的生词本中 ---->保存map结构
//    {
//        PrintWriter output=null;	// 输出流,保存所有的生词本单词到文件,使用于自测面板
//        int i=0;
//        try {
//            output=new PrintWriter("我的生词本.txt");	//输出流定位的文件
//            for(String key : mywords.keySet()){
//                output.print(key+" "+mywords.get(key)+" ");
//            }
//        } catch (FileNotFoundException e) {
//            // TODO Auto-generated catch block
//            e.printStackTrace();
//        }
//        finally
//        {
//            output.close();
//        }
//    }




}


class Word	//单词类
{
    String word;	//单词
    String character;	//翻译

}
class Dictionary	//字典类（所有单词的集合）
{
    ArrayList <Word> words=new ArrayList<>();	//字典类含有单词的集合
    String filename;
    Dictionary(String f)//在构造Dictionary对象时初始化
    {
        filename = f;//调用下面函数从文件中读取单词和汉字
    }
    public void addWords(String f)//文件路径名称,初始化word类数据,文件为空不要紧，因为使用SCanner读取next没有就不会继续处理
    {
        Scanner input=null;
        try {
            input=new Scanner(new File(f),"utf-8");	//单词的文本文件
            while(input.hasNext())
            {
                Word word=new Word();
                word.word=input.next();		//单词文本文件赋给单词的英文
                word.character=input.next();	//汉字的文本文件赋给单词的翻译
                words.add(word);	//把单词添加到单词集合中
            }
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();//在命令行打印异常信息在程序中出错的位置及原因
        }
        finally
        {
            input.close();	//  关闭流
        }
    }
    public void saveWords()		//  保存单词进度函数,保存指定的进度到不同的单词文件中,四级六级文件，保存list结构
    {
        PrintWriter output=null;	//   输出流
        int i=0;
        int k =0;
        try {
            output=new PrintWriter(new OutputStreamWriter(
                    new FileOutputStream( filename),
                    "UTF-8"));
            // 输出流定位的文件,全部写入
            while(i<words.size())		//  把未删除的单词输出到定位文件中
            {
                k++;
                output.print(words.get(i).word+" "+words.get(i).character+" ");//get(i)获取Arraylist对应的元素
                if(k % 5 ==0){
                    output.print("\n");
                }
                i++;
            }
        } catch (FileNotFoundException | UnsupportedEncodingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        finally
        {
            output.close();
        }
    }


}
