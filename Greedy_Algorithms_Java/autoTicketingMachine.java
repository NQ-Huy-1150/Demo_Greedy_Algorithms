package Greedy_Algorithms;
import java.util.ArrayList;
import java.util.Scanner;
//gia ve duong sat bac nam
public class autoTicketingMachine {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //bang gia ve
        int number = 0, price = 0, count = 0, sum = 0, customer = 0;
        System.out.println ("Bảng giá vé Hà Nội - Sài Gòn của tàu SE7");
        System.out.println("1: Nằm khoang 4 điều hoà T2 : 1,609,000đ");
        System.out.println("2: Nằm khoang 6 điều hoà T1 : 1,444,000đ");
        System.out.println("3: Nằm khoang 6 điều hoà T3 : 1,146,000đ");
        System.out.println("4: Ngồi mềm điều hoà        : 966,000đ");
        System.out.println("5: Ngồi cứng điều hoà       : 744,000đ");
        System.out.println("6: Ghế phụ                  : 524,000đ");
        // user input
        System.out.print ("Ban chon loai ve nao : ");
        number = scanner.nextInt();
        System.out.print("Nhập vào số lượng vé bạn muốn mua : ");
        count = scanner.nextInt();
        switch (number) {
            case 1:
                price = 1609;
                break;
            case 2:
                price = 1444;
                break;
            case 3:
                price = 1146;
                break;
            case 4:
                price = 966;
                break;
            case 5:
                price = 744;
                break;
            default:
                price = 524;
                break;
        }
        sum = price * count;
        // in hoa don va xac nhan thanh toan
        System.out.printf("Hoá đơn của bạn (đơn vị K vnđ) : %d K\n",sum);
        do{
            System.out.printf("Hãy nhập vào số tiền bạn muốn thanh toán (> %d K) : ",sum);
            customer = scanner.nextInt();
            if (customer < sum) System.out.println("Số tiền cần phải thanh toán không đủ, vui lòng kiểm tra lại !");
        }while(customer < sum); // dam bao so tien thanh toan can phai >= hoa don

        // tinh tien tra cho khach va quy doi tien te
        int amount = customer - sum;
        System.out.printf("so tien can phai tra lai cho khach hang : %d K\n",amount);
        int[] arr = {500, 200, 100, 50, 20, 10, 5, 2, 1};
        ArrayList<String> a = new ArrayList<>(); // log file
        int cnt = 0; // dem so luong to tien
        for (int i = 0; i < arr.length; i++) {
            int temp = amount/arr[i];
            cnt += temp;
            if (temp != 0) {
                a.add(temp + " x " + arr[i] + "K ");
            }
            amount %= arr[i];
        }
        // in ra so to tien it nhat can phai tra cho khach
        System.out.printf("So to phai tra cho khach : %d\n",cnt);
        // in ra log de kiem tra lai
        System.out.println(a);
        scanner.close();
    }
}
