int addition(int a, int b) {
	int c;
	c = a + b;
	return c;
}

int main(void) {
	int i, sum, n[3];

	sum = 0;
	n[1] = 5;

	for(i = 0; i < n[1]; i++) {
		sum = addition(sum, i);
	}

	printf("%d", sum);
}
