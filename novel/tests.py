from django.test import TestCase

# Create your tests here.


def test_print(num):
    print("ASd-{}".format(num))

def test_write(num):
    with open("a_{}.txt".format(num), "a", encoding="utf-8")as fp:
        fp.write("Asdads\n")