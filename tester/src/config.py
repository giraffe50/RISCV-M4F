"""Configuration file

Filename: config.py
Author: SunnyChen
"""
from pyhcl import *

# ------------------------------------------------------------------ #
# Basic Parameters
# ------------------------------------------------------------------ #
WLEN = 32
BLEN = 8
RLEN = 5        # Register number's width
INSTCACHE_SIZE = 4096
REGFILE_LEN = 32
# M_Mode = 3

# ------------------------------------------------------------------ #
# Control signal width
# ------------------------------------------------------------------ #
PC_WRITE_SIG_WIDTH = 1
PC_SEL_SIG_WIDTH = 2
IF_ID_WRITE_SIG_WIDTH = 1
IF_IF_FLUSH_SIG_WIDTH = 1
REG_WRITE_SIG_WIDTH = 1
IMM_SEL_SIG_WIDTH = 3
ALU_SRC_SIG_LEN = 1
ALUOP_SIG_LEN = 5
BRANCH_SIG_LEN = 1
BRANCH_SRC_SIG_LEN = 1
MEM_READ_SIG_LEN = 1
MEM_WRITE_SIG_LEN = 1
DATA_SIZE_SIG_LEN = 2
LOAD_TYPE_SIG_LEN = 1
REG_SRC_SIG_LEN = 3
JUMP_TYPE_SIG_LEN = 1
BUBBLE_SIG_LEN = 1
ID_EX_FLUSH_SIG_LEN = 1
CONFLAG_SIG_LEN = 1
FORWARD_A_SIG_LEN = 2
FORWARD_B_SIG_LEN = 2
MEMWRITE_SRC_SIG_LEN = 1
DATA_CACHE_LEN = 32
PC_SRC_SIG_LEN = 1
IF_ID_FLUSH_SIG_LEN = 1

# ================================================================== #
# Main control signals
# ================================================================== #

# ------------------------------------------------------------------ #
# PC_Sel
# ------------------------------------------------------------------ #
PC_Sel_pc_4 = U.w(2)(0)
PC_Sel_pc_recover = U.w(2)(1)
PC_Sel_new_addr = U.w(2)(2)

# ------------------------------------------------------------------ #
# Register write
# ------------------------------------------------------------------ #
Reg_Write_False = U.w(1)(0)
Reg_Write_True = U.w(1)(1)

# ------------------------------------------------------------------ #
# Imm_Sel
# ------------------------------------------------------------------ #
IMM_X = U.w(3)(0)
IMM_R = U.w(3)(1)
IMM_I = U.w(3)(2)
IMM_S = U.w(3)(3)
IMM_SB = U.w(3)(4)
IMM_U = U.w(3)(5)
IMM_UJ = U.w(3)(6)

# ------------------------------------------------------------------ #
# ALU_Src
# ------------------------------------------------------------------ #
ALU_B_XXX = U.w(1)(0)
ALU_B_rs2 = U.w(1)(0)
ALU_B_imm = U.w(1)(1)

# ------------------------------------------------------------------ #
# ALU_Op
# ------------------------------------------------------------------ #
ALU_ADD = U.w(5)(0)
ALU_SUB = U.w(5)(1)
ALU_AND = U.w(5)(2)
ALU_OR = U.w(5)(3)
ALU_XOR = U.w(5)(4)
ALU_SLL = U.w(5)(5)
ALU_SRL = U.w(5)(6)
ALU_SRA = U.w(5)(7)
ALU_SLT = U.w(5)(8)
ALU_SLTU = U.w(5)(9)
ALU_BEQ = U.w(5)(10)
ALU_BNE = U.w(5)(11)
ALU_BLT = U.w(5)(12)
ALU_BGE = U.w(5)(13)
ALU_BLTU = U.w(5)(14)
ALU_BGEU = U.w(5)(15)
ALU_OP_XXX = U.w(5)(16)

# ------------------------------------------------------------------ #
# Branch
# ------------------------------------------------------------------ #
Branch_False = U.w(1)(0)
Branch_True = U.w(1)(1)

# ------------------------------------------------------------------ #
# Branch_Src
# ------------------------------------------------------------------ #
Branch_XXX = U.w(1)(0)
Branch_PC = U.w(1)(0)
Branch_Rs1 = U.w(1)(1)

# ------------------------------------------------------------------ #
# Jump_Type
# ------------------------------------------------------------------ #
Conditional = U.w(1)(0)
NonConditional = U.w(1)(1)

# ------------------------------------------------------------------ #
# Mem_Read
# ------------------------------------------------------------------ #
Mem_Read_False = U.w(1)(0)
Mem_Read_True = U.w(1)(1)

# ------------------------------------------------------------------ #
# Mem_Write
# ------------------------------------------------------------------ #
Mem_Write_False = U.w(1)(0)
Mem_Write_True = U.w(1)(1)

# ------------------------------------------------------------------ #
# Data size
# ------------------------------------------------------------------ #
Data_Size_W = U.w(2)(0)
Data_Size_H = U.w(2)(1)
Data_Size_B = U.w(2)(2)

# ------------------------------------------------------------------ #
# Memory load type
# ------------------------------------------------------------------ #
Load_XXX = U.w(1)(0)
Load_Signed = U.w(1)(0)
Load_Unsigned = U.w(1)(1)

# ------------------------------------------------------------------ #
# Memory to register source
# ------------------------------------------------------------------ #
RegWrite_XXX = U.w(3)(0)
RegWrite_ALU = U.w(3)(0)
RegWrite_Mem = U.w(3)(1)
RegWrite_PC_4 = U.w(3)(2)
RegWrite_imm = U.w(3)(3)
RegWrite_ipc = U.w(3)(4)

# ================================================================== #
# Hazard detection unit signal
# ================================================================== #

# ------------------------------------------------------------------ #
# Bubble
# ------------------------------------------------------------------ #
Bubble_False = U.w(1)(0)
Bubble_True = U.w(1)(1)

# ------------------------------------------------------------------ #
# IF/ID register write
# ------------------------------------------------------------------ #
IF_ID_Write_False = U.w(1)(0)
IF_ID_Write_True = U.w(1)(1)

# ------------------------------------------------------------------ #
# PC_Write
# ------------------------------------------------------------------ #
PC_Write_False = U.w(1)(0)
PC_Write_True = U.w(1)(1)

# ================================================================== #
# Forward unit signal
# ================================================================== #

# ------------------------------------------------------------------ #
# Forward A signal
# ------------------------------------------------------------------ #
Forward_A_rs1 = U.w(2)(0)
Forward_A_mem_wb_rd = U.w(2)(1)
Forward_A_ex_mem_rd = U.w(2)(2)

# ------------------------------------------------------------------ #
# Forward B signal
# ------------------------------------------------------------------ #
Forward_B_rs1 = U.w(2)(0)
Forward_B_mem_wb_rd = U.w(2)(1)
Forward_B_ex_mem_rd = U.w(2)(2)

# ------------------------------------------------------------------ #
# Memory forward signal
# ------------------------------------------------------------------ #
MemWrite_Src_rs2 = U.w(1)(0)
MemWrite_Src_wb = U.w(1)(1)

# ================================================================== #
# Memory cache load signal
# ================================================================== #
Word_Signed = U.w(3)(0)
Word_Unsigned = U.w(3)(1)
HWord_Signed = U.w(3)(2)
HWord_Unsigned = U.w(3)(3)
Byte_Signed = U.w(3)(4)
Byte_Unsigned = U.w(3)(5)

# ================================================================== #
# Address buffer write index
# ================================================================== #
Write_0 = U.w(2)(0)
Write_1 = U.w(2)(1)
Write_2 = U.w(2)(2)

# ================================================================== #
# Branch predictor signal
# ================================================================== #

# ------------------------------------------------------------------ #
# IF_ID_Flush signal
# ------------------------------------------------------------------ #
IF_ID_Flush_False = U.w(1)(0)
IF_ID_Flush_True = U.w(1)(1)

# ------------------------------------------------------------------ #
# ID_EX_Flush signal
# ------------------------------------------------------------------ #
ID_EX_Flush_False = U.w(1)(0)
ID_EX_Flush_True = U.w(1)(1)

# ------------------------------------------------------------------ #
# 2-bit dynamic saturating counter status
# ------------------------------------------------------------------ #
Strong_Nottaken = U.w(2)(0)
Weak_Nottaken = U.w(2)(1)
Strong_Taken = U.w(2)(2)
Weak_Taken = U.w(2)(3)


# ================================================================== #
# CSR unit signal
# ================================================================== #

# ------------------------------------------------------------------ #
# CSR is_Exception Signal
# ------------------------------------------------------------------ #
is_Exception_False = U.w(2)(0)
is_Exception_MEPC  = U.w(2)(1)
is_Exception_MTVEC = U.w(2)(2)

# ------------------------------------------------------------------ #
# CSR addrs
# ------------------------------------------------------------------ #
mstatus_addr    = U.w(12)(768)
mie_addr        = U.w(12)(772)
mtvec_addr      = U.w(12)(773)
mepc_addr       = U.w(12)(833)
mcause_addr     = U.w(12)(834)
mtval_addr      = U.w(12)(835)
mip_addr        = U.w(12)(836)
mtime_addr      = U.w(12)(1792)
mtimeh_addr     = U.w(12)(1793)
mtimecmp_addr   = U.w(12)(1794)
mtimecmph_addr  = U.w(12)(1795)
mcycle_addr     = U.w(12)(2816)
mcycleh_addr    = U.w(12)(2944)
minstret_addr   = U.w(12)(2818)
minstreth_addr  = U.w(12)(2946)

# mstatus_addr    = "001100000000"
# mie_addr        = "001100000100"
# mtvec_addr      = "001100000101"
# mepc_addr       = "001101000001"
# mcause_addr     = "001101000010"
# mtval_addr      = "001101000011"
# mip_addr        = "001101000100"
# mtime_addr      = "011100000000"
# mtimeh_addr     = "011100000001"
# mtimecmp_addr   = "011100000010"
# mtimecmph_addr  = "011100000011"
# mcycle_addr     = "101100000000"
# mcycleh_addr    = "101110000000"
# minstret_addr   = "101100000010"
# minstreth_addr  = "101110000010"

# ------------------------------------------------------------------ #
# CSR Exceptions
# ------------------------------------------------------------------ #
InstructionAddrMisaligned = U(0)
IllegalInstruction        = U(2)
LoadAddressMisaligned     = U(4)
StoreAddressMisaligned    = U(6)

# ------------------------------------------------------------------ #
# CSR Interrupts
# ------------------------------------------------------------------ #
MachineTimerInterrupt     = U(7)
ExternalInterrupt         = U(8)

# ------------------------------------------------------------------ #
# CSR control signal's width
# ------------------------------------------------------------------ #
WRITE_CSR_SIG_LEN = 3
IS_ILLEGAL_SIG_LEN = 1
EX_MEM_FLUSH_SIG_LEN = 1
IS_EXCEPTION_SIG_LEN = 2
CSR_SRC_SIG_LEN = 1
EXCEPTION_FLUSH_SIG_LEN = 1
PREDICT_FAILED_SIG_LEN = 1
MIE_ENABLE_SIG_LEN = 1
ID_EX_WRITE_SIG_LEN = 1

# ------------------------------------------------------------------ #
# CSR CSR_src
# ------------------------------------------------------------------ #
RegWrite_CSR = U.w(3)(5)

CSR_src_XXX = U.w(1)(0)
CSR_src_rs1 = U.w(1)(0)
CSR_src_imm = U.w(1)(1)

# ------------------------------------------------------------------ #
# CSR Write_CSR
# ------------------------------------------------------------------ #
Write_CSR_False   = U.w(3)(0)
Write_CSR_True_W  = U.w(3)(1)
Write_CSR_True_WI = U.w(3)(2)
Write_CSR_True_S  = U.w(3)(3)
Write_CSR_True_SI = U.w(3)(4)
Write_CSR_True_C  = U.w(3)(5)
Write_CSR_True_CI = U.w(3)(6)
Write_CSR_Return  = U.w(3)(7)

# ------------------------------------------------------------------ #
# CSR is_Illegal
# ------------------------------------------------------------------ #
is_Illegal_False = U.w(1)(0)
is_Illegal_True  = U.w(1)(1)

