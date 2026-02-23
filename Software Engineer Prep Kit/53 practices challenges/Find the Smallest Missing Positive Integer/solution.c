int findSmallestMissingPositive(int orderNumbers_count, int* orderNumbers) {
    int i;
    int temp=0;
    for(i=0;i<=orderNumbers_count-1;i++){
        while(orderNumbers[i]>0&&orderNumbers[i]<=orderNumbers_count&&orderNumbers[orderNumbers[i]-1]!=orderNumbers[i]){
            temp=orderNumbers[i];
            orderNumbers[i]=orderNumbers[orderNumbers[i]-1];
            orderNumbers[temp-1]=temp;
        }
    }
    i=0;
    int man=1;
    while(orderNumbers[i]==i+1 && i<=orderNumbers_count-1){
        i++;
        man=man+1;
    }
    return man;
}