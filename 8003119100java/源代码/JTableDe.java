package day4;

import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.FileNotFoundException;
import javax.swing.*;
import java.util.*;
import java.io.*;
//查看单词表

//public class wordsTtable extends JFrame {
//    public wordsTtable() {
//
//        this.setLocation(500, 300);
//        this.setSize(300, 300);
//        this.setLayout(null);
//        JButton bu1 = new JButton("选择文件");
//        bu1.setBounds(0, 0, 300, 200);
//        bu1.setIcon(new ImageIcon("image/choicewords.png"));
//        this.add(bu1);
//        this.setVisible(true);
//        bu1.addMouseListener(new MouseAdapter() {
//            public void mouseClicked(MouseEvent e) {
//                JFileChooser fd = new JFileChooser();
//                fd.setFileSelectionMode(JFileChooser.OPEN_DIALOG);
//                fd.showOpenDialog(null);
//                File f = fd.getSelectedFile();
//                String filepath = f.getPath().trim();
//                JTableDe dictionary_table = new JTableDe(filepath);
//
//            }
//
//        });
//    }
//
//    public static void main(String[] args) {
//        new wordsTtable();
//    }
//}


 class JTableDe extends JFrame {
    void createComponent(String f){

        this.setTitle(f);
        this.setLocation(600, 300);
        this.setSize(500, 800);
        this.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        Container contentPane = this.getContentPane();
        Object[][] tableDate = new Object[300][2];
        Map<String, String> map = new TreeMap<String, String>
                (new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) { //定义按照字母顺序排序方法
                return o1.compareTo(o2);
            }
        });

        int i = 0;
        Scanner input = null;
        try {
            input = new Scanner(new File(f),"utf-8");
            while (input.hasNext()) {
                map.put(input.next(), input.next());
            }
        } catch (FileNotFoundException e2) {
            e2.printStackTrace();
        } finally {
            input.close();
        }
        Set<String> keySet = map.keySet();
        Iterator<String> iter = keySet.iterator();
        while (iter.hasNext()) {
            String key = iter.next();
            tableDate[i][0] = key;
            tableDate[i++][1] = map.get(key);//最后按照字母顺序排列
        }
        String[] name = {"英文", "中文"};
        JTable table = new JTable(tableDate, name);// 创建表格
        contentPane.add(new JScrollPane(table));
        this.setVisible(true);
    }

}


