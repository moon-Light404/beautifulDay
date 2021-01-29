package day4;
import java.awt.*;
import javax.swing.*;
public class Window extends JFrame{
    recitePanel recitewords;
    checkPanel checkwords;
    challengePanel chall;
    JPanel info;
    JLabel label,label1,label2;

    public Window(){
        info = new JPanel(null);
        label = new JLabel("名称:单词学习系统");
        label1 = new JLabel("作者:丁俊");
        label2 = new JLabel("学号:8003119100");
        label.setFont(new Font(null, Font.PLAIN, 30));
        label1.setFont(new Font(null, Font.PLAIN, 30));
        label2.setFont(new Font(null, Font.PLAIN, 30));

        label.setBounds(130,40,400,100);
        label1.setBounds(130,80,200,100);
        label2.setBounds(130,120,400,100);

        info.add(label);
        info.add(label1);
        info.add(label2);
        setLocation(400,100);
        setSize(650,600);
        recitewords = new recitePanel();
        checkwords = new checkPanel();
        chall = new challengePanel();
        JTabbedPane AllTable = new JTabbedPane();
        AllTable.add(recitewords,"背单词");
        AllTable.add(checkwords,"查单词");
        AllTable.add(chall,"深度学习");
        AllTable.add(info,"版本信息");
        this.add(AllTable);
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.setVisible(true);
        this.setTitle("单词学习系统");
    }
}
