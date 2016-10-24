'''
This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
def half_pyramid (rows):
	for r in range(1, rows + 1):
		for c in range(1, r + 1):
			print(c, end=" ")
		print()

def main():
	i = ask_input()
#	half_pyramid(i)
	pyramid(i)

def ask_input():
	i = int(input('How many rows in the Pyramid? '))
	return i

def pyramid (rows):
	indent = rows
	for r in range(1, rows + 1):
		for i in range(0, indent):
			print(' ', end=' ')
		indent -= 1
		for c in range((-r) + 1, r):
			print(abs(c), end=' ')
		print()

main()
