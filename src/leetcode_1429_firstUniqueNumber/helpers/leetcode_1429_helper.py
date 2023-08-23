class FunctionHelper:
    def __init__(self, instance=None, nums=[]):
        self.res = []
        if not instance:
            self.res = []
        else:
            self.res = [None]
        self.instance = instance(nums)

    def run(self, method_names, method_args):
        for method_name, method_arg in zip(method_names, method_args):
            method = getattr(self.instance, method_name)
            self.res.append(method(*method_arg))
        return self.res
