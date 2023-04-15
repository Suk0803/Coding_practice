import java.util.*;

public class Main {    
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int[] A = new int[N];
		
		for (int i = 0; i < N; i++) {
			A[i] = in.nextInt();
			
		}
		// int형 스택선언
		Stack<Integer> stack = new Stack<>();
		StringBuffer bf = new StringBuffer();
		
		int num = 1;
		boolean result = true;
		
		for (int i = 0; i <A.length; i++ ) {
			int su = A[i]; // 현제 수열 의 수
			// 현제수열 값>= 오름차순 자연수 : 값이 같아질때 까지 push() 수행
			if(su >= num ) {
				while (su >= num) {
					stack.push(num++);
					bf.append("+\n");
				}
				stack.pop();
				bf.append("-\n");
			
			} else {
				// 현제 수열 값 < 오름차순 자연수 : pop() 을 수행하여 수열 원소를 꺼냅니다.
				int n = stack.pop();
				// 스택의 가장 위의 수가 만들어야하는 수열의 수보다 크다면 출력 불가능
				if (n > su) {
					System.out.println("NO");
					result = false;
					break;
				} else {
					bf.append("-\n");
				}
			}
			
		}
			
		if (result) System.out.println(bf.toString());
        
    }
}
