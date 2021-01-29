package day4;

import javax.swing.*;
import javax.tools.Tool;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.io.*;
import java.lang.management.BufferPoolMXBean;
import java.util.*;
import java.util.regex.Pattern;

public class checkPanel extends JTabbedPane implements ActionListener {
    JPanel check;
    JPanel checkwords;
    JButton button1;
    JButton button2;
    JButton button4; // 清空按钮
    JLabel l1,l2;
    JLabel tip;
    JTextField textChi,textEng;
    String [] Books = new String[]{"无","四级","六级","我的生词本","字典"};
    JComboBox<String> libe = new JComboBox<String>(Books);
    maptools tool = new maptools();// 定义方法类，方便调用其中的方法
    Map<String, String> map;// 存储Allwords.txt文件




    checkPanel () {//设置组件和面板初始化
         this.map = new HashMap<>();
         tool.checkBegin(map,"file/Allwords.txt"); // 从总文件字典中读取单词信息
         check = new JPanel();
         check.setLayout(null);
         check.setLayout(new FlowLayout(FlowLayout.CENTER));
         checkwords = new JPanel();
        button1 = new JButton("英译汉");
        button1.setPreferredSize(new Dimension(120,40));
        button2 = new JButton("汉译英");
        button2.setPreferredSize(new Dimension(120,40));
//        button3 = new JButton("选择文件");
//        button3.setPreferredSize(new Dimension(100,50));
        button4 = new JButton("清空");
        button4.setBackground(Color.GREEN);
        l1=new JLabel("中文");
        l1.setBounds(30,5,60,30);
        l1.setFont(new Font("黑体",Font.PLAIN,18));
        l2 = new JLabel("英文");
        l2.setFont(new Font("黑体",Font.PLAIN,18));
        l2.setBounds(30,70,60,30);
        tip = new JLabel("选择文件:");
        textEng = new JTextField(20);
        textEng.setBounds(95,5,200,30);
        textEng.setFont(new Font("黑体",Font.PLAIN,20));

        textChi = new JTextField(20);
        textChi.setBounds(95,40,200,300);
         textChi.setFont(new Font("黑体",Font.PLAIN,20));


        //监听器
        button1.addActionListener(this);
        button2.addActionListener(this);
//        button3.addActionListener(this);
         libe.addItemListener(new ItemListener() {
             @Override
             public void itemStateChanged(ItemEvent e) {
                 int index =libe.getSelectedIndex();
                 if(e.getStateChange() == ItemEvent.SELECTED) {
                     switch (index) {
                         case 0: // 打开四级单词表

                             break;
                         case 1:
                             createList("file/四级.txt");
                             break;
                         case 2:
                             createList("file/六级.txt");
                             break;
                         case 3:
                             createList("file/我的生词本.txt");
                             break;
                         case 4:
                             createList("file/Allwords.txt");
                             break;
                         default:
                             break;
                     }
                 }
             }
         });
        button4.addActionListener(this);
        //窗口
        check.add(l1);
        check.add(textChi);
         check.add(l2);
         check.add(textEng);
         check.add(button2);
         check.add(button1);
         check.add(button4);
         checkwords.add(tip);
         checkwords.add(libe);

         this.add(check,"翻译");
         this.add(checkwords,"查看所有单词");
    }


        public void createList(String filename){
         try {
             JTableDe dic = new JTableDe();
             dic.createComponent(filename); // 创建单词表格
         }catch (Exception e2){
             e2.printStackTrace();
         }
        }

    public void actionPerformed(ActionEvent e) {

//        if (str == null || str.isEmpty()) {
//            JOptionPane.showMessageDialog(this, "请输入要查询的单词", null, JOptionPane.WARNING_MESSAGE);
//            return;
//        }
        if (e.getSource() == button1) {//英语-->汉语
            String str = this.textEng.getText();
            String mean1 = this.map.get(str);
            if (mean1 == null) {
                JOptionPane.showMessageDialog(this, "没有查到您输入的单词", null, JOptionPane.WARNING_MESSAGE);
                return;
            } else {
                this.textChi.setText(mean1);
            }
        } else if (e.getSource() == button2) {//中文翻译英文
            String str2=this.textChi.getText();
            String meaning2 = tool.getKeyByValue(this.map, str2);
            if (meaning2 == " ") {
                JOptionPane.showMessageDialog(this, "没有查到您输入的单词", null, JOptionPane.WARNING_MESSAGE);
                return;
            } else
                this.textEng.setText((String) meaning2);
        }

        else if(e.getSource() == button4){
            textChi.setText(null);
            textEng.setText(null);
        }
    }




}


