import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BF10972 {

    private static int[] input;
    private static boolean[] isSelected;
    private static int[] p;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        input = new int[N];
        p = new int[N];
        isSelected = new boolean[N];

        for (int i = 0; i < N; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }
        dic(0, N);
    }

    public static void dic(int count, int N) {
        if (count == N) System.out.println(Arrays.toString(p));

        for (int i = 0; i < N; i++) {
            if (isSelected[i]) continue;
            p[count] = i + 1;
            isSelected[i] = true;
            if (Arrays.toString(p).equals(Arrays.toString(input))) {
                System.out.println("OK");
            }
            dic(count + 1, N);
            isSelected[i] = false;
        }
    }

}
