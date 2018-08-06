## Trick and explanation
## http://www.purplemath.com/modules/base_why.htm

"""convert positive integer to base 2"""
def binarify(num): 
	if num <= 0:
		return "Error" ## we will learn error handling later in course
		
	digits = []
	while num > 0:
		digits.append(num % 2)
		num = num / 2

	#assigns digits the sequence from the first to the last
	#element in digits, starting with the last one.
	digits = digits[::-1] 
	
	#.join() concatenates
	return ''.join(str(i) for i in digits)


"""convert positive integer to a string in any base"""
def int_to_base(num, base):
    if num <= 0 or base <= 0:
        return "Error"
    if base == 10:
        return str(num)
    if base == 1:
        return "1" * num
    else:
    	digits = []
    	while num > 0:
    		digits.append(num % base)
    		num = num / base
    	digits = digits[::-1]
    	return ''.join(str(i) for i in digits)


"""take a string-formatted number and its base and return the base-10 integer"""
def base_to_int(string, base):
	if string == "0" or base <= 0:
		return "Error"
	
	result = 0
	exp = len(string)
	for i in string:
		exp -= 1 ## to what power?
		result += ((base ** exp) * int(i))
	
	return result


"""add two numbers of different bases and return the sum"""
def flexibase_add(str1, str2, base1, base2):
	return base_to_int(str1, base1) + base_to_int(str2, base2)


"""multiply two numbers of different bases and return the product"""
def flexibase_multiply(str1, str2, base1, base2):
	return base_to_int(str1, base1) * base_to_int(str2, base2)


"""given an integer, return the Roman numeral version"""
def romanify(num):
  if(num < 0 or num > 3999):
  	return "Error"
  
  ans = ""
  
  while num >= 1000:
  	ans += "M"
  	num -= 1000

  while num >= 900:
  	ans += "CM"
  	num -= 900

  while num >= 500:
  	ans += "D"
  	num -= 500

  while num >= 400:
  	ans += "CD"
  	num -= 400
  	
  while num >= 100:
  	ans += "C"
  	num -= 100
  
  while num >= 90:
  	ans += "XC"
  	num -= 90
  
  while num >= 50:
  	ans += "L"
  	num -= 50
  
  while num >= 40:
  	ans += "XL"
  	num -= 40
  
  while num >= 10:
  	ans += "X"
  	num -= 10
  
  while num >= 9:
  	ans += "IX"
  	num -= 9
  
  while num >= 5:
  	ans += "V"
  	num -= 5
  
  while num >= 4:
  	ans += "IV"
  	num -= 4
  
  while num >= 1:
  	ans += "I"
  	num =- 1

  return ans

  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.