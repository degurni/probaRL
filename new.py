
# https://github.com/sergio12S/youtoube/tree/master
# 1 https://www.youtube.com/watch?v=Dwnzhk34vhM
# 2 https://www.youtube.com/watch?v=_wZoyDdbK6M&list=PLRoQmvSf6MgwTuiZ8BDVCf8GBQ_Szt6Ci&index=3
# 3 https://www.youtube.com/watch?v=GZ6vsai8T0M&list=PLRoQmvSf6MgwTuiZ8BDVCf8GBQ_Szt6Ci&index=4
# 4 https://www.youtube.com/watch?v=m_pmjaL_srg&list=PLRoQmvSf6MgwTuiZ8BDVCf8GBQ_Szt6Ci&index=5
# 5 https://www.youtube.com/watch?v=1tWCsRq0Ymc&list=PLRoQmvSf6MgwTuiZ8BDVCf8GBQ_Szt6Ci&index=6

from envirenment import Environment
from dataset import Dataset



# f = Dataset().get_datas(50, ['BTCUSDT', 'ETHUSDT'], '15m')


env = Environment('BTCUSDT', ['close'], 30)

print(env.reset())

print(env.bar)
