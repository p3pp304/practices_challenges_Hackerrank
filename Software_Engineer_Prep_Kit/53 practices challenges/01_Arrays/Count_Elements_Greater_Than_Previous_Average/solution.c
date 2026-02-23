int countResponseTimeRegressions(int responseTimes_count, int* responseTimes) {
    if (responseTimes_count == 0) {
        return 0;
    }
    int n=responseTimes_count-1;
    double somma=responseTimes[0];
    double average;
    int i;
    int count=0;
    for(i=1;i<=n;i++){
        average=somma/i;
        if(responseTimes[i]>average){
            count++;
        }
        somma+=responseTimes[i];
    }
    return count;
}