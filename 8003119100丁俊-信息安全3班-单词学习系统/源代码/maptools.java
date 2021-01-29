package day4;

import java.io.*;
import java.util.*;
import java.util.regex.Pattern;

// 处理存储单词的map文件数据和方法
public class maptools{
    ArrayList<String> temp_list = new ArrayList<String>(); // 记录临时选择的值，防止重复

    Random ran = new Random(); // 随机变量
    String pattern1 = "[A-Za-z]+";//  英文
    String pattern2 = "[\u4E00-\u9FA5]+";//  中文
    // 根据中文获取英文
    public String getKeyByValue(Map map, String value) {
        Iterator it = map.entrySet().iterator();
        Map.Entry entry = null;
        boolean isfind = false;
        while (it.hasNext()) {
            entry = (Map.Entry) it.next();
            Object obj = entry.getValue();
            if (value.equals(obj)) {
                isfind = true;
                break;
            }
        }
        if (isfind == true)
            return (String) entry.getKey();
        else
            return " ";
    }


    // 初始化map单词键值对
    public void checkBegin(Map map,String f) {
        Scanner readin = null;
        try {
            readin = new Scanner(new File(f),"utf-8");//指定翻译单词的文件字典
            while (readin.hasNext()) {
                map.put(readin.next(), readin.next());//读取单词表到map中
            }
        } catch (FileNotFoundException e1) {
            e1.printStackTrace();
        } finally {
            readin.close();
        }
    }

    // 从map中随机选取四个值
    public ArrayList<String> select_four(Map map){ // 随机选取四个值
        ArrayList<String> return_list = new ArrayList<String>(); // 准备返回的数组
        String[] keys = (String[]) map.keySet().toArray(new String[0]);
        String rankey = null;
        int time = 0;
        while(time<4) { //循环四次
            rankey = keys[ran.nextInt(keys.length)];
            while (is_inlist(temp_list, rankey)) { // 当选中的key在列表中
                rankey = keys[ran.nextInt(keys.length)];
//                System.out.println(rankey);
            }
            time++;
            return_list.add(rankey);
            temp_list.add(rankey);
        }
        temp_list.clear();
        return return_list;
    }


    //  判断某个元素是否在list数组中
    public Boolean is_inlist(ArrayList list,Object obj){
        if(list.contains(obj)){
            return true;
        }
        else{
            return false;
        }
    }

    public void savetoFile(String key,String value,String fileName){//  把单词保存到任意文件
        try {
            FileOutputStream writer = new FileOutputStream(fileName, true);// 追加文件
            writer.write((" "+ key+ " " + value + " ").getBytes("utf-8"));
            // 把单词加到生词本当中去
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //添加文件到指定文件和map中
    public Boolean CollectWords(Map map,String key,String value,String fileName) {
        if(!map.containsKey(key)) {
            //   myword中不包含这个键(单词),则添加到文件
            map.put(key,value);//   先把单词信息添加到mywords中
            savetoFile(key,value,fileName);//  保存到文件
            return true; // 收藏成功
        }
        else{//如果单词重复了
            return false;// 收藏失败
        }
    }

    public Boolean isChi(String str){//  判断是否是中文
        boolean isMatch = Pattern.matches(pattern2,str);
        return isMatch;
    }
    public Boolean isEng(String str){//  判断是否是英文
        boolean isMatch = Pattern.matches(pattern1,str);
        return isMatch;
    }

    public void saveMaptoFile(Map newmap,String filename)		// 保存单词进度函数 ---->保存map结构
    {
        int i = 1;
        PrintWriter output=null;	// 输出流,保存所有的生词本单词到文件,使用于自测面板
        try {
            output=new PrintWriter(new OutputStreamWriter(
                    new FileOutputStream( filename),
                    "UTF-8"));	//输出流定位的文件
            for(Object key : newmap.keySet()){
                i++;
                output.print(key+" "+newmap.get(key)+" ");
                if(i% 5 == 0){
                    output.print("\n");
                }
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