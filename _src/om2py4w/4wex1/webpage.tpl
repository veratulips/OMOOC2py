<html>
<head>
	<title> Diary-web </title>
</head>
<body>
	<p>请输入日记内容:</p>
	<form action="/diary" method="POST">
		<input type="text" size="100" maxlength="100" name="filename">
		<input type="submit" name="save" value="save">
	</form>
	<ul>
		%for line in input:
		{{line}}
		%end
	</ul>
</body>
</html>