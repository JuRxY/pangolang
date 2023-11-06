import pangolang

# SHELL STARTUP
print("Pangolang v1.2, Oct 19 2023, 18:20:26 UTC)")

# SHELL LOOP
while True:
	text = input('>>> ')
	if text.strip() == "": continue
	result, error = pangolang.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print("Exit status: " + repr(result.elements[0]))
		else:
			print(repr(result))