public class profitlosscalculator {
    public static void main(String[] args) {
        double cost = 121;
        double sellingprice = 191;

        double proftORloss = sellingprice - cost;
        double percentage = (proftORloss/cost)*100;

        System.out.println("The costprice is "+ cost + "The selling price is "+ sellingprice );
        System.out.println("Profit or Loss: $" + proftORloss);
        System.out.printf("Percentage of Profit or Loss: %.2f%%%n", percentage);
    }
    
}
