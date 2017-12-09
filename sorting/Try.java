import java.awt.*;
import javax.swing.*;
import java.util.Scanner;
import java.util.Arrays;

public class Try extends JPanel {

    static String output = "";

    public static void swap(int[] array, int x, int y){    
        int tmp = array[x];
        array[x] = array[y];
        array[y] = tmp;
    }

    public static void swap(long[] array, int x, int y){    
        long tmp = array[x];
        array[x] = array[y];
        array[y] = tmp;
    }

    public static void record(int[] array){
        for(int e : array){
            output += Integer.toString(e) + " ";
        }
        output += "\n";
    }

    public static void record(long[] array){
        for(long e : array){
            output += String.valueOf(e) + " ";
        }
        output += "\n";
    }

    public static void record_char(int[] array){
        for(int e : array){
            output += (char)e;
        }
        output += "\n";
    }
//*********************sorting function*********************//
    public static void bubbleSort(long[] array){
        
        for(int i=0;i<array.length;i++){
            for(int j=0;j<array.length-i-1;j++){
                if(array[j]>array[j+1]){
                    swap(array,j,j+1);
                    record(array);
                }
            }
        }
    }

    public static void selectionSort(int[] array){

        for(int i=0;i<array.length-1;i++){
            int min = i;
            for(int j=i+1;j<array.length;j++){
                if(array[j]<array[min]){
                    min = j;
                }
            }
            if(min!=i){
                swap(array,i,min);
                record_char(array);
            }
            
        }
    }

    public static void insertionSort(long[] array){
        int j;
        for(int i=1;i<array.length;i++){
            long tmp = array[i];
            for(j=i;j>0 && tmp<array[j-1];j--){
                array[j] = array[j-1];
            }
            array[j]=tmp;
            record(array);
        }
    }

    public static void quickSort(int[] array,int left,int right){

        if (right <= left)
            return;
 
      

        // middle pivot
        int pivotIndex = (left+right)/2;
        int pivot = array[pivotIndex];
        // swap pivot to right
        swap(array,pivotIndex,right);
        int swapIndex = left;
        for(int i=left;i<right;i++){
            //smaller than privot , swap to left
            //and left index will plus 1 
            if(array[i]<=pivot){
                swap(array,i,swapIndex);
                swapIndex++;
                // record(array);
            }
        }
        swap(array,swapIndex,right);
        record(array);
        quickSort(array,left,swapIndex-1);
        quickSort(array,swapIndex+1,right);

    }

    public static void radixSort(int[] array){

        

    }
//*********************sorting function*********************//

    public Try() {

    }
    
 
    public static void main(String[] args) {
        // SwingUtilities.invokeLater(() -> {
        JFrame f = new JFrame();
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//可以按左上角叉叉關閉
        f.setTitle("yiyu");
        f.setResizable(false);
        // f.add(new Try(), BorderLayout.CENTER);//從中間加入
        // f.pack();//setSize與pack,前者為手動設定,後者為自動調整
        f.setSize(800,600);
        f.setLocationRelativeTo(null);//開啟與某物件相同 null 代表從中間開啟
        
        JTextField input0 = new JTextField(10);
        JPanel myPanel0 = new JPanel();
        myPanel0.setLayout(new GridLayout(2,1));
        myPanel0.add(new JLabel("請選擇你要哪一種排序法 1)insertionSort 2)selectionSort 3)bubbleSort 4)quickSort 5)radixSort"));
        myPanel0.add(input0);
        int result0 = JOptionPane.showConfirmDialog(null, myPanel0,"Please Enter data", JOptionPane.OK_CANCEL_OPTION);


        JTextField input = new JTextField(10);
        JPanel myPanel = new JPanel();
        myPanel.setLayout(new GridLayout(2,1));
        myPanel.add(new JLabel("請輸入需排序的資料"));
        myPanel.add(input);

        int result = JOptionPane.showConfirmDialog(null, myPanel,"Please Enter data", JOptionPane.OK_CANCEL_OPTION);
       

        //if(result == JOptionPane.OK_OPTION){
        //    System.out.println("value: " + input.getText());
        
        String usrData = input.getText();
        

        String option = input0.getText();

        if(result == JOptionPane.OK_OPTION){
            System.out.println("value: " + input.getText());
        }else{
            System.exit(0);
        }

        if(option.equals("1")){
            //only accept number


            String [] splitData = usrData.split(" ");
            long [] unsortedData = new long [splitData.length];

            //translate to int
            for(int i=0;i<splitData.length;i++)
                unsortedData[i] = Long.parseLong((splitData[i]));

            // check data
            // for(int e : unsortedData)
            //     System.out.print(e);

         
            
            insertionSort(unsortedData);
        }else if(option.equals("2")){
            //accept alphabat and number


            // String [] splitData = usrData.split("");
            int [] unsortedData = new int [usrData.length()];
            for(int i=0;i<usrData.length();i++)
                unsortedData[i] = (int)(usrData.charAt(i));

            selectionSort(unsortedData);            
        }else if(option.equals("3")){

            String [] splitData = usrData.split(" ");
            long [] unsortedData = new long [splitData.length];

            //translate to int
            for(int i=0;i<splitData.length;i++)
                unsortedData[i] = Long.parseLong(splitData[i]);

            // check data
            // for(int e : unsortedData)
            //     System.out.print(e);

            
            bubbleSort(unsortedData);

        }else if(option.equals("4")){
            
            String [] splitData = usrData.split(" ");
            int [] unsortedData = new int [splitData.length];

            //translate to int
            for(int i=0;i<splitData.length;i++)
                unsortedData[i] = Integer.parseInt(splitData[i]);

            // check data
            // for(int e : unsortedData)
            //     System.out.print(e);

            for(int i=0;i<splitData.length;i++)
                unsortedData[i] = Integer.parseInt(splitData[i]);
            quickSort(unsortedData,0,unsortedData.length-1);    
        }else if(option.equals("5")){
            
            // String [] splitData = usrData.split(",");
            // int [] unsortedData = new int [splitData.length];

            // //translate to int
            // for(int i=0;i<splitData.length;i++)
            //     unsortedData[i] = Integer.parseInt(splitData[i]);

            // // check data
            // // for(int e : unsortedData)
            // //     System.out.print(e);

            // for(int i=0;i<splitData.length;i++)
            //     unsortedData[i] = Integer.parseInt(splitData[i]);
            // radixSort(unsortedData);    
        }


        f.add(new JTextArea(output));
        f.setVisible(true);

    }
}
