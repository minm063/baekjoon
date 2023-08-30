import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BF10448 {

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] result = new int[N];

        for (int i = 0; i < N; i++) {
            int K = Integer.parseInt(br.readLine());
            // n*(n+1)/2=1000, n=45

            for (int j = 1; j < 45; j++) {
                for (int k = 1; k < 45; k++) {
                    for (int m = 1; m < 45; m++) {
                        int sum = Tn(j) + Tn(k) + Tn(m);
                        if (sum == K) {
                            result[i] = 1;
                            break;
                        }
                    }
                }
            }
        }
        for (int i = 0; i < N; i++) {
            System.out.println(result[i]);
        }
    }

    public static int Tn(int n) {
        return n * (n + 1) / 2;
    }

}
