#def lcsm(): Finding a Shared Motif

if __name__ == "__main__":
    
    import os, sys

    lcsmFile = "rosalind.txt"

    f = open(lcsmFile)
    lcsmSeq = f.readlines()
    print(lcsmSeq[0:10])
    f.close()

    # Step1: Seq_name + \n + seq + \n reform
    
    whole_seq = []
    long_seq = []
    rosalind_seq = ' '
    
    whole_seq.append(lcsmSeq[0])            #1 첫 리스트에서 읽어들인 값을 이름으로 
    
    for i in lcsmSeq[1:]:                            # 첫번째 행은 rosalin 이름이므로 제외하고, 2번째 행부터 시작
        long_seq.append(i.strip("\n"))          # 행바꿈 기호를 제거한 후 long_seq 리스트에 아이템 추가
        rosalind_seq = ''.join(long_seq)         # long_seq 의 아이템으로 추가되니 아이템끼리 join 하여 seq 서열 만들어 rosalind_seq에 추가
        if i.startswith('>'):                            # rosalin name 인 행을 읽었을때는 지난 리스트 및 변수를 정리함
            whole_seq.append(rosalind_seq[:-14]+"\n")   # >가 있는 기호까지 읽었기 때문에 해당 이름을 제거한 값만 #1 다음행에 whole 리스트에 추가
            whole_seq.append(i)                    # 현재 읽어들인 행값인 name 을 추가
            rosalind_seq =  ' '                        # rosalind_seq 변수를 비움
            long_seq.clear()                          # long_seq 리스트를 비움
            print('rosalind)_seq & long_seq values are changed')
        else:
            pass
    whole_seq.append(rosalind_seq)              # 제일 마지막 rosalind seq 값을 list에 추가 (else 문으로 빠져나온 값)
    
    file = open('rosalind_seq_non-N.txt', 'w')   # 각 서열마다의 \N 값을 제거한 seq file 새로 만들기
    for i in whole_seq:
        file.write(i)
    file.close()
    
    # Step2: Seq1 quary combination list formation (k mer number input)

    quary_list = []
    print('input predicted k mer =')
    
    k = int(sys.stdin.readline())

    Quary_Numbers = len(whole_seq[1])-k
    
    for i in range(Quary_Numbers):
        quary_list.append(whole_seq[1][i:i+k])     # stdin 에서 입력받은 숫자에 해당하는 kmer를 첫번째 whole_seq[1]으로부터 만듬
        

    # Step3: Mapping

    for i in whole_seq[2:]:
        if i.startswith('>'):
            pass
        else:
            for w in range(Quary_Numbers):
                if quary_list[w] in i:
                    print('matched')
                    print(quary_list[w])
                
   
