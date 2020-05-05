def solution(s):
	lc_norm = [i for i in range(97, 123)]
	lc_rev = [j for j in range(122, 96, -1)]
	dict_lc = {lc_norm[n]: lc_rev[n] for n in range(len(lc_norm))}

	decrypted_s = []

	for c in s:
		if dict_lc.has_key(ord(c)):
			decrypted_s.append(chr(dict_lc[ord(c)]))
		else:
			decrypted_s.append(c)

	return ''.join(decrypted_s)
