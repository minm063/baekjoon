import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Greedy1449 {

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        int[] loc = new int[1001];
        int answer = 0;
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < n; i++) {
            // 1 1 0 ... 0 1 1 ...
            loc[Integer.parseInt(st.nextToken())] = 1;
        }

        for (int i = 0; i <= 1000; i++) {
            if (loc[i] != 0) {
                i += L - 1;
                answer++;
            }
        }
        System.out.println(answer);
    }

    public static int[] swap(int[] loc) {
        int n = loc.length;
        for (int i = 0, j = i; i < n - 1; j = ++i) {
            int next = loc[i + 1];
            while (next < loc[j]) {
                loc[j + 1] = loc[j];
                if (j-- == 0) {
                    break;
                }
            }
            loc[j + 1] = next;
        }
        return loc;
    }
}
