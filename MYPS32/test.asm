.text
main:
    addi $s5, $s5, 1  # ajoutes les différente valeur de s1, s2, s3
    addi $s4, $s4, 2
    addi $s3, $s3, 3
loop:
    sll $t0, $s3, 2    #t0 = 4*1
    add $t0, $t0, $s6  #t0 -> save[i]; t0 = 1000 2000 + 4*i
    lw $t0, 0, ($t0)     #t0 = save[i]
    bne $t0, $s5, EXIT   #goto exit si save[i] != k
    add $s3, $s3, $s4    #i = i + j
    j loop
exit: 
    jr $ra