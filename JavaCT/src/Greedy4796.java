import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Greedy4796 {
    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = 1;
        StringBuilder sb = new StringBuilder();

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            int L = Integer.parseInt(st.nextToken());
            int P = Integer.parseInt(st.nextToken());
            int V = Integer.parseInt(st.nextToken());

            if (L == 0 || P == 0 || V == 0) {
                break;
            }

            // �����ϴ� 8(P)�� �� 5(L)�ϵ��ȸ� ��� ����. ���� �� 20(V)��¥�� �ް��� ����
            // ķ������ �ִ� ��ĥ���� ����� �� �ֳ�?
            // 8 �� 5, 8 �� 5 (������� 16��)
            // 8 �� 4�� -> 14�� ��� ����

            int testCase = L * (V / P) + Math.min(L, V % P);
            sb.append("Case ").append(n).append(": ").append(testCase).append("\n");
            n++;
        }
        System.out.print(sb);
    }

}
