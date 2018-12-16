int addition(int a, int b) {
	int c;
	c = a + b;
	return c;
}

int nsqr(int a, int n) {
	int t, ret;

	if(n <= 0) {
		ret = 1;
	}
	if(n > 0) {
		ret =  a * nsqr(a, n - 1);
	}

	return ret;
}

int main(void) {
	int a, b;

	a = 5;
	b = nsqr(a, 3);

	printf("%d", b);
}