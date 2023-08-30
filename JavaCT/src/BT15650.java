import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BT15650 {

    private static int N;
    private static int M;
    private static int[] result;

    public static void main(String[] args) throws IOException {
        // 1 ~ N pick M
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        result = new int[M];

        dic(0, 1);
    }

    public static void dic(int count, int start) {
        if (count == M) {
            System.out.println(Arrays.toString(result).replaceAll("\\[|\\]|\\,", ""));
            return;
        }
        for (int i = start; i <= N; i++) {
            result[count] = i;
            dic(count + 1, i + 1);
        }
    }

}
