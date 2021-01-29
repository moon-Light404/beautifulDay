package day4;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.util.*;

public class challengePanel extends JTabbedPane implements ActionListener{
    String newfile; // 选择的文件
    Map<String, String> map1 = new HashMap<>();// 存储选中的单词数据
    Map<String,String> myEng = new HashMap<>(); // 存储我的生词本单词
    maptools Tool = new maptools(); // 创建map处理对象
    String [] t = new String[4]; // 选中的四个单词
    ArrayList<String> temp = new ArrayList<String>();

    // 第一个面板
    JPanel p = new JPanel();
    JTextField English = new JTextField(25);; // 英文框
    JRadioButton  d1 = new JRadioButton(" ",true);
    JRadioButton d2 = new JRadioButton();
    JRadioButton d3 = new JRadioButton();
    JRadioButton d4 = new JRadioButton();
    JButton bu_ac; // 确认单词
    JButton collect; // 收藏单词
    ButtonGroup bp;

    JLabel show_score = new JLabel();  // 答对一个单词得10分
    int score = 0;
    Boolean isStart = false;

    String [] choice = new String[]{"无","四级","六级","我的生词本"};
    JComboBox<String> choices;
    Random random = new Random(); // 随机变量


    // 第二个面板，修改单词
    JButton bu_change,bu_yes;
    JPanel p1 = new JPanel();
    JTextField f1,f2; // 中文和英文
    JLabel g1,g2; // 中文标识框
    JLabel litip; // 请选择单词表




    public void action(){
        if(map1.size()>=4) {
            temp = Tool.select_four(map1);// 四个单词的英文
            for(int i=0;i<4;i++){
                t[i] = map1.get(temp.get(i));
            } // 选出了四个单词中文

            English.setText(Tool.getKeyByValue(map1,t[random.nextInt(t.length)]));
            // 随机选一个中文

            d1.setText(t[0]);
            d2.setText(t[1]);
            d3.setText(t[2]);
            d4.setText(t[3]);
        }else{
            JOptionPane.showMessageDialog(this, "单词少于四个哦", null, JOptionPane.INFORMATION_MESSAGE);
        }
/*
        for(Map.Entry<String,String> entry: map1.entrySet()){
            System.out.println(entry.getKey()+entry.getValue());
        }
*/
    }

    challengePanel(){
        Tool.checkBegin(myEng,"file/我的生词本.txt");// 从我的生词本中读取单词到 myEng中
        p.setLayout(null);
        p1.setLayout(null);
        litip = new JLabel("请选择单词表:");
        litip.setBounds(310,30,100,25);
        choices = new JComboBox<>(choice); // 添加到单选框中
        choices.setBounds(310,60,70,25);

         choices.addItemListener(new ItemListener() {
             @Override
             public void itemStateChanged(ItemEvent e) {
                 int index = choices.getSelectedIndex();
                 // 判断所选内容
                 if (e.getStateChange() == ItemEvent.SELECTED){
                     // 加一个if可以防止弹出两次窗口
                     switch (index) {
                         case 0:
                             break;
                         case 1:
                             isStart = true;
                             map1.clear(); // 清空上一次的存储
                             newfile = "file/四级.txt";
                             Tool.checkBegin(map1, newfile);

                             action();
                             break;
                         case 2:
                             isStart = true;
                             map1.clear();// 清空上一次的存储
                             newfile = "file/六级.txt";
                             Tool.checkBegin(map1, newfile);

                             action();
                             break;
                         case 3:
                             isStart = true;
                             map1.clear();// 清空上一次的存储
                             newfile = "file/我的生词本.txt";
                             Tool.checkBegin(map1, newfile);

                             action();
                             break;

                     }
             }

             }
         });


        bu_ac = new JButton("确定");
        bu_ac.setBounds(250,150,70,25);

        collect = new JButton("收藏");
        collect.setBounds(250,200,70,25);

        d1.setFont(new Font("宋体", Font.PLAIN, 20));

        d2.setFont(new Font("宋体", Font.PLAIN, 20));

        d3.setFont(new Font("宋体", Font.PLAIN, 20));

        d4.setFont(new Font("宋体", Font.PLAIN, 20));
        bp = new ButtonGroup();
        d1.setBounds(100,120,150,25);
        d2.setBounds(100,150,150,25);
        d3.setBounds(100,180,150,25);
        d4.setBounds(100,210,150,25);
        bp.add(d1);
        bp.add(d2);
        bp.add(d3);
        bp.add(d4);
        bu_ac.addActionListener(this);
        collect.addActionListener(this);



        English.setEnabled(false);
        English.setFont(new Font("黑体", Font.PLAIN, 25));
        English.setBounds(100,60,200,30);

        show_score.setBounds(100,30,150,30);


        p.add(show_score);
        p.add(English);
        p.add(d1);
        p.add(d2);
        p.add(d3);
        p.add(d4);
        p.add(bu_ac);
        p.add(litip);
        p.add(choices);
        p.add(collect);
        this.add(p,"选单词");
        this.add(p1,"修改");

        f1 = new JTextField();
        f1.setFont(new Font("黑体", Font.PLAIN, 25));
        f1.setBounds(100,60,200,30);

        f2 = new JTextField();
        f2.setFont(new Font("黑体", Font.PLAIN, 25));
        f2.setBounds(100,100,200,30);

        g1 = new JLabel("中文");
        g2 = new JLabel("英文");
        g1.setFont(new Font("黑体", Font.PLAIN, 18));
        g2.setFont(new Font("黑体", Font.PLAIN, 18));
        g2.setBounds(60,60,40,25);
        g1.setBounds(60,100,40,25);

        bu_change = new JButton("修改");
        bu_change.setBounds(120,140,70,25);
        bu_yes = new JButton("我确认了");
        bu_yes.setBounds(200,140,90,25);

        bu_change.addActionListener(this);
        bu_yes.addActionListener(this);


        p1.add(f1);
        p1.add(f2);
        p1.add(bu_change);
        p1.add(bu_yes);
        p1.add(g1);
        p1.add(g2);

    }
    public void actionPerformed(ActionEvent e){
        if(e.getSource() == bu_ac && isStart) {
            for (Component c : p.getComponents()) {
                if (c instanceof JRadioButton && ((JRadioButton) c).isSelected()) {
                    if (((JRadioButton) c).getText().equals(map1.get(English.getText()))) {
                        this.action();
                        score = score + 10; // 答对一题加10分
                        show_score.setText("当前分数"+"  "+ score);
                    } else {
                        JOptionPane.showMessageDialog(this, "回答错误", null, JOptionPane.INFORMATION_MESSAGE);
                    }

                }
            }
        }
        // 收录English框中的单词
        else if(e.getSource() == collect && isStart){
            if(Tool.CollectWords(myEng, English.getText(),map1.get(English.getText()),"file/我的生词本.txt" )){
                JOptionPane.showMessageDialog(this,"收藏成功",null,JOptionPane.INFORMATION_MESSAGE);
            }
            else{
                JOptionPane.showMessageDialog(this,"已收录该单词",null,JOptionPane.INFORMATION_MESSAGE);
            }
        }

        else if(e.getSource() == bu_change){
            if(map1.containsKey(f1.getText())){ // 在map1中存在该单词
                if(f2.getText()!=null && Tool.isChi(f2.getText())){  // 输入的为中文
                    map1.put(f1.getText(),f2.getText()); // 修改map1的value
                    JOptionPane.showMessageDialog(this,"修改成功"+f1.getText()+"--"+f2.getText(),null,JOptionPane.INFORMATION_MESSAGE);
                }
                else{
                    JOptionPane.showMessageDialog(this,"为空或非格式错误",null,JOptionPane.INFORMATION_MESSAGE);
                }
            }
            else{
                JOptionPane.showMessageDialog(this,"没找到该单词",null,JOptionPane.INFORMATION_MESSAGE);
            }
        }
        else if(e.getSource() == bu_yes){ // 确认修改操作
            if(isStart){
                Tool.saveMaptoFile(map1,newfile);
                JOptionPane.showMessageDialog(this,"保存修改成功",null,JOptionPane.INFORMATION_MESSAGE);
            }
        }
    }



//    public static void main(String[] args) {
//        challenge ch = new challenge();
//    }
}
