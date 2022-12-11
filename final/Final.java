// STEP: Import required packages
import java.sql.*;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.File;

public class Final {
    private Connection c = null;
    private String dbName;
    private boolean isConnected = false;

    private void openConnection(String _dbName) {
        dbName = _dbName;

        if (false == isConnected) {
            System.out.println("++++++++++++++++++++++++++++++++++");
            System.out.println("Open database: " + _dbName);

            try {
                String connStr = new String("jdbc:sqlite:");
                connStr = connStr + _dbName;

                // STEP: Register JDBC driver
                Class.forName("org.sqlite.JDBC");

                // STEP: Open a connection
                c = DriverManager.getConnection(connStr);

                // STEP: Diable auto transactions
                c.setAutoCommit(false);

                isConnected = true;
                System.out.println("success");
            } catch (Exception e) {
                System.err.println(e.getClass().getName() + ": " + e.getMessage());
                System.exit(0);
            }

            System.out.println("++++++++++++++++++++++++++++++++++");
        }
    }

    private void closeConnection() {
        if (true == isConnected) {
            System.out.println("++++++++++++++++++++++++++++++++++");
            System.out.println("Close database: " + dbName);

            try {
                // STEP: Close connection
                c.close();

                isConnected = false;
                dbName = "";
                System.out.println("success");
            } catch (Exception e) {
                System.err.println(e.getClass().getName() + ": " + e.getMessage());
                System.exit(0);
            }

            System.out.println("++++++++++++++++++++++++++++++++++");
        }
    }


    private void build_data_cube() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("BUILD DATA CUBE");


        System.out.println("++++++++++++++++++++++++++++++++++");
    }


    private void print_Product() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("PRINT PRODUCT");

        System.out.printf("%-20s %-20s %-20s\n", "model", "type", "maker");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void print_Distributor() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("PRINT DISTRIBUTOR");

        System.out.printf("%-20s %-20s %20s\n", "model", "name", "price");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void print_Cube() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("PRINT DATA CUBE");

        System.out.printf("%-20s %-20s %10s %10s\n", "dist", "prod", "cnt", "total");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }


    private void modifications() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("MODIFICATIONS");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }


    public static void main(String args[]) {
        Final sj = new Final();
        
        sj.openConnection("data.sqlite");

        sj.print_Product();
        sj.print_Distributor();

        sj.build_data_cube();
        sj.print_Cube();

        sj.modifications();

        sj.print_Product();
        sj.print_Distributor();
        sj.print_Cube();

        sj.closeConnection();
    }
}
