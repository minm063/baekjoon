import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Greedy11047 {
    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split(" ");
        int n = Integer.parseInt(arr[0]), k = Integer.parseInt(arr[1]), count = 0;
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(br.readLine());
        }
        while (n > 0) {
            if (k < a[n - 1]) {
                n--;
                continue;
            }
            k -= a[n - 1];
            count++;
        }
        System.out.println(count);
    }

}
