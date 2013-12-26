# coding=utf-8

from unittest import TestCase
import fibonacci
from examples.fibonacci import arbitrary_arguments


class BasicTypesTests(TestCase):
    def test_numbers(self):
        # simple numbers
        self.assertEquals(2 * 2, 4)

        # imaginary items
        # complex numbers inlude real and imaginary part
        self.assertEquals(1j, 1J)

        self.assertEquals(round(1.5), 2)

    def test_strings(self):
        # simple strings
        self.assertEquals("string", 'string')

        self.assertEquals('A' + 'B', 'AB')

        self.assertEquals('String'[2:4], 'ri')
        self.assertEquals('String'[2:], 'ring')
        self.assertEquals('String'[-1], 'g')
        self.assertEquals(len('String'), 6)

        # only first symbol is capitalized
        self.assertEquals('fString'.capitalize(), 'Fstring')

        self.assertTrue('str' in 'string')

        self.assertEquals(u'строка', u'строка')

    def test_lists(self):
        list = ['1', '2', 3, 4, 5]

        self.assertEquals(len(list), 5)

        self.assertEquals(list[3:], [4, 5])

        list.append(6)

        self.assertEquals(list[5], 6)

    def test_control_flow_if(self):
        list = [0, 1, 2]

        if list[0] == 0 and list[1] == 1:
            list.append(2)
        elif list[0] == 1:
            list[0] = 2
        else:
            list[0] = 3

    def test_control_flow_for(self):
        list = [0, 1, 2]

        for item in list:
            list[0] = item

    def test_range(self):
        list = range(3, 6)

        self.assertEquals(list, [3, 4, 5])

    def test_pass(self):
        for item in range(1, 2):
            """ The pass statement does nothing. It can be used when a statement is required syntactically
            but the program requires no action."""
            pass

    def test_using_functions(self):
        sequence = fibonacci.fibonacci(9)

        self.assertEquals(sequence, [0, 1, 1, 2, 3, 5, 8])

    def test_arbitrary_arguments(self):
        self.assertEquals(arbitrary_arguments('1', '2', '3', '4'), '1-2-3-4')
