class Helper:
    def run_methods(self, instance: any, method_names: list[str], method_args: list[list[int]]) -> list[int]:
        if not instance:
            return []

        output = [None]

        for method_name, method_arg in zip(method_names[1:], method_args[1:]):
            method = getattr(instance, method_name)
            output.append(method(*method_arg))

        return output
        
        



