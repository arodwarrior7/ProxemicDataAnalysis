class CrowdType:

    def __init__(self, crowd_description: str = ''):
        self.crowd_description: str = crowd_description
        self.crowd_data: list = [list] * 3
        self.crowd_data[0] = list()
        self.crowd_data[1] = list()
        self.crowd_data[2] = list()
        self.first_data_min: float = 0.0
        self.first_data_max: float = 0.0
        self.first_data_mean_min: float = 0.0
        self.first_data_mean_max: float = 0.0
        self.second_data_min: float = 0.0
        self.second_data_max: float = 0.0
        self.second_data_mean_min: float = 0.0
        self.second_data_mean_max: float = 0.0
        self.third_data_min: float = 0.0
        self.third_data_max: float = 0.0
        self.third_data_mean_min: float = 0.0
        self.third_data_mean_max: float = 0.0
        self.all_data_min: float = 0.0
        self.all_data_max: float = 0.0
        self.all_data_mean_min: float = 0.0
        self.all_data_mean_max: float = 0.0
        self.full_data_crowd: list = [list] * 3
        self.full_data_crowd[0] = list()
        self.full_data_crowd[1] = list()
        self.full_data_crowd[2] = list()
        self.full_data_crowd_all_mean: float = 0.0
        self.full_data_crowd_first_mean: float = 0.0
        self.full_data_crowd_second_mean: float = 0.0
        self.full_data_crowd_third_mean: float = 0.0

    def print_crowdtype_info(self):
        print('crowd_description: ' + self.crowd_description)
        print('crowd_data: ' + str(self.crowd_data))
        print('crowd_data[0] size: ' + str(len(self.crowd_data[0])))
        print('crowd_data[1] size: ' + str(len(self.crowd_data[1])))
        print('crowd_data[2] size: ' + str(len(self.crowd_data[2])))
        print('crowd_data size: ' + str((len(self.crowd_data[0])+len(self.crowd_data[1])+len(self.crowd_data[2]))))
        print('first_data_min: ' + str(self.first_data_min))
        print('first_data_max: ' + str(self.first_data_max))
        print('first_data_mean_min: ' + str(self.first_data_mean_min))
        print('first_data_mean_max: ' + str(self.first_data_mean_max))
        print('second_data_min: ' + str(self.second_data_min))
        print('second_data_max: ' + str(self.second_data_max))
        print('second_data_mean_min: ' + str(self.second_data_mean_min))
        print('second_data_mean_max: ' + str(self.second_data_mean_max))
        print('third_data_min: ' + str(self.third_data_min))
        print('third_data_max: ' + str(self.third_data_max))
        print('third_data_mean_min: ' + str(self.third_data_mean_min))
        print('third_data_mean_max: ' + str(self.third_data_mean_max))
        print('all_data_min: ' + str(self.all_data_min))
        print('all_data_max: ' + str(self.all_data_max))
        print('all_data_mean_min: ' + str(self.all_data_mean_min))
        print('all_data_mean_max: ' + str(self.all_data_mean_max))
        print('full size: ' + str(len(self.full_data_crowd)))
        print('full_data_crowd[0] mean: ' + str(self.full_data_crowd_first_mean))
        print('full_data_crowd[1] mean: ' + str(self.full_data_crowd_second_mean))
        print('full_data_crowd[2] mean: ' + str(self.full_data_crowd_third_mean))
        print('full_data_crowd all mean: ' + str(self.full_data_crowd_all_mean))
