int process(int *arr) {
  int sum = 0;
  for (int i = 0; i < 5; i++)
    if (arr[i] % 2)
      sum += arr[i];
    else
      sum += arr[i] * 2;
  return sum;
}
