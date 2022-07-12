from asyncio import run_coroutine_threadsafe
from concurrent.futures import process
from socket import CAN_RAW
from turtle import st


class Trip :
    id          = int
    user        = str
    car         = str
    route       = str
    amount      = int
    payment     = int
    process     = str
    complete    = str