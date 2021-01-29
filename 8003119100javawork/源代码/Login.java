package day4;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Login extends JFrame implements ActionListener{
    JLabel userName,password;
    JPanel myPanel;
    ImageIcon background ;
    JLabel label;
    JTextField userId;
    JPasswordField passId;
    JButton bu1;
    JLabel name,id,author,secret;

    Login(){
        init();
    }
    void init(){
        name = new JLabel("作品:单词学习系统");
        name.setFont(new Font("宋体",Font.PLAIN,20));
        id = new JLabel("学号:8003119100");
        id.setFont(new Font("宋体",Font.PLAIN,20));
        author = new JLabel("作者:丁俊");
        author.setFont(new Font("宋体",Font.PLAIN,20));
        name.setBounds(0,0,200,100);
        author.setBounds(0,20,200,100);
        id.setBounds(0,40,200,100);

        secret = new JLabel("密码:123");
        secret.setBounds(0,60,200,100);
        secret.setFont(new Font("宋体",Font.PLAIN,18));


        userName = new JLabel("账号:");
        userName.setFont(new Font("宋体",Font.PLAIN,18));
        userName.setForeground(Color.green);
        userName.setBounds(250,150,100,25);

        password = new JLabel("密码:");
        password.setFont(new Font("宋体",Font.PLAIN,18));
        password.setForeground(Color.green);
        password.setBounds(250,200,100,25);

        userId = new JTextField();
        userId.setBounds(300,150,150,25);
        userId.setFont(new Font("黑体", Font.PLAIN, 20));

        passId= new JPasswordField();
        passId.setBounds(300,200,150,25);
        passId.setFont(new Font("黑体", Font.PLAIN, 20));

        bu1=new JButton("登录");
        bu1.setBounds(310,250,70,25);
        bu1.addActionListener(this);

        //设置背景图片
        this.setLayout(null);
        background = new ImageIcon("image/java1.png");
        label = new JLabel(background);// 把背景图片添加到标签里
        label.setBounds(0,0,background.getIconWidth(),background.getIconHeight());

        myPanel = (JPanel)this.getContentPane();//把我的面板设置为内容面板
        myPanel.setOpaque(false);//  把我的面板设置为不可视
        myPanel.setLayout(null);
        this.getLayeredPane().setLayout(null);
        myPanel.add(userName);// 把组件加进到面板当中
        myPanel.add(password);
        myPanel.add(userId);
        myPanel.add(passId);
        myPanel.add(bu1);
        myPanel.add(name);
        myPanel.add(author);
        myPanel.add(id);
        myPanel.add(secret);
        this.getLayeredPane().add(label, new Integer(Integer.MIN_VALUE));


        this.setBounds(400, 100,background.getIconWidth() , background.getIconHeight());
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setVisible(true);
    }
    public void actionPerformed(ActionEvent e){
        if(e.getSource() == bu1){
            String Id = userId.getText();//获取账号
            String pass = new String(passId.getPassword());//获取密码

            if(Id.equals("丁俊") ){
                if(pass.equals("123")){
                    JOptionPane.showMessageDialog(this,"登陆成功",
                            null,JOptionPane.INFORMATION_MESSAGE);
                    this.setVisible(false);   //  登录框消失
                    Window win = new Window();   //  进入界面
                }
                else{
                    JOptionPane.showMessageDialog(this,"密码错误",
                            null,JOptionPane.INFORMATION_MESSAGE);

                }
            }
            else{
                JOptionPane.showMessageDialog(this,"用户名输入错误",
                        null,JOptionPane.INFORMATION_MESSAGE);
            }
        }
    }

    public static void main(String[] args) {
        Login login = new Login();
    }

}
