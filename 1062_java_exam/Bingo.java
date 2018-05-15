import java.util.Random;
import java.util.Scanner;
class Board{

	private int [][] board = new int [5][5];
	private int [][] flag = new int [5][5];

	Board(){
		Random ran = new Random();

		for(int i=0;i<5;i++){
			for(int j=0;j<5;j++){
				int nowRan = ran.nextInt(25)+1;
				if(!inBoard(nowRan)){
					this.board[i][j] = nowRan;
				}else{
					j--;
					continue;
				}
			}
		}
	}
	boolean inBoard(int ran){
		for(int i=0;i<5;i++){
			for(int j=0;j<5;j++){
				if(ran == board[i][j]){
					return true;
				}
			}
		}
		return false;
	}


	void print(){
		for(int i=0;i<5;i++){
			for(int j=0;j<5;j++){
				if(flag[i][j]==1)
					System.out.printf("%02d ",board[i][j]);
				else
					System.out.printf("** ");
			}
			System.out.println();
		}
	}

	boolean wasGuessed(int yourGuess){
		for(int i=0;i<5;i++){
			for(int j=0;j<5;j++){
				if(board[i][j]==yourGuess){
					if(flag[i][j]==1){
						return true;
					}else{
						flag[i][j]=1;
					}
				}
			}
		}
		return false;
	}

	boolean win(){
		int line = 0;
		/*
		1 1 1 1 1         0 0 0 0 0 
		0 0 0 0 0         0 0 0 0 0 
		0 0 0 0 0   ~~~   0 0 0 0 0 
		0 0 0 0 0         0 0 0 0 0 
		0 0 0 0 0         1 1 1 1 1 
		*/
		for(int i=0;i<5;i++){
			boolean holder = true;
			for(int j=0;j<5;j++){
				if(flag[i][j]==0){
					holder = false;
					break;
				}
			}

			if(holder)
				line++;
		}
		/*
		1 0 0 0 0         0 0 0 0 1
		1 0 0 0 0         0 0 0 0 1
		1 0 0 0 0   ~~~   0 0 0 0 1
		1 0 0 0 0         0 0 0 0 1
		1 0 0 0 0         0 0 0 0 1
		*/
		for(int i=0;i<5;i++){
			boolean holder = true;
			for(int j=0;j<5;j++){
				if(flag[j][i]==0){
					holder = false;
				}
			}

			if(holder)
				line++;
		}
		/*
		1 0 0 0 0
		0 1 0 0 0
		0 0 1 0 0
		0 0 0 1 0
		0 0 0 0 1
		*/
		if(flag[0][0]==flag[1][1]&&
		   flag[1][1]==flag[2][2]&&
		   flag[2][2]==flag[3][3]&&
		   flag[3][3]==flag[4][4]&&
		   flag[4][4]==1){
			line++;
		}
		/*
		0 0 0 0 1
		0 0 0 1 0
		0 0 1 0 0
		0 1 0 0 0
		1 0 0 0 0
		*/
		if(flag[0][4]==flag[1][3]&&
		   flag[1][3]==flag[2][2]&&
		   flag[2][2]==flag[3][1]&&
		   flag[3][1]==flag[4][0]&&
		   flag[4][0]==1){
			line++;
		}
		// System.out.println("Line: "+line);
		if(line>=12){
			return true;
		}
		return false;
	}

}

public class Bingo{

	public static void main(String[] args) {
		Board b = new Board();
		Scanner sc = new Scanner(System.in);
		int playingTime = 0;
		System.out.println("Game start!");
		while(true){

			System.out.print("Your guess : ");
			int yourGuess = sc.nextInt();
			System.out.println();
			if(yourGuess<1 || yourGuess>25){
				System.out.println("You have wrong gussing number, please change another one.");
				continue;
			}
			if(b.wasGuessed(yourGuess)){
				System.out.println("You have gussed this number, please change another one.");
				continue;
			}
			b.print();
			playingTime++;
			if(b.win()){
				System.out.println("Bingo! You have guessed "+playingTime+" times.");
				break;
			}
		}
	}
}