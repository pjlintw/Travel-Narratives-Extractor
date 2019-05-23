
file_name = 'test_with_ground_truth.tsv'
file = open(file_name,'r', encoding='utf-8').readlines()

wf = open('val.txt', 'w', encoding='utf-8')
for line in file:
	_, label, _, text = line.strip().split('\t')
	text = ''.join([ token for token in text if token != ' '])
	
	wf.write(f'{label} {text}\n')

wf.close()
