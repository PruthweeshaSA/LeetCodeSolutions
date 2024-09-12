class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        variable_values = {}
        component = {}
        vars_in_component = {}

        max_component_index = 1.0

        equation = equations[0]
        var0 = equation[0]
        var1 = equation[1]

        variable_values[var1] = max_component_index
        variable_values[var0] = values[0] * variable_values[var1] 
        
        component[var0] = max_component_index
        component[var1] = max_component_index
        vars_in_component[max_component_index] = set()
        vars_in_component[max_component_index].add(var0)
        vars_in_component[max_component_index].add(var1)
        

        for i in range(1,len(equations)):
            equation = equations[i]
            var0 = equation[0]
            var1 = equation[1]
            if var0 not in component and var1 not in component:
                max_component_index += 1.0
                variable_values[var1] = max_component_index
                variable_values[var0] = values[i] * variable_values[var1]
                print(f"{(var0,var1)}= {(variable_values[var0],variable_values[var1])}")
                component[var1] = max_component_index
                component[var0] = max_component_index
                vars_in_component[max_component_index] = set()
                vars_in_component[max_component_index].add(var0)
                vars_in_component[max_component_index].add(var1)
            elif var0 not in component:
                component_index = component[var1]
                variable_values[var0] = values[i] * variable_values[var1] 
                component[var0] = component_index
                vars_in_component[component_index].add(var0)
            elif var1 not in component:
                component_index = component[var0]
                variable_values[var1] = variable_values[var0] / values[i]
                component[var1] = component_index
                vars_in_component[component_index].add(var1)
            elif component[var0] > component[var1]:
                higher_component = component[var0]
                lower_component = component[var1]
                hc_var_set = vars_in_component[higher_component]
                expected_value = values[i] * variable_values[var1]
                actual_value = variable_values[var0]
                collapsefactor = expected_value / actual_value
                while len(hc_var_set)>0:
                    var_to_collapse = hc_var_set.pop()
                    variable_values[var_to_collapse] = variable_values[var_to_collapse] * collapsefactor
                    component[var_to_collapse] = lower_component
                vars_in_component.pop(higher_component)
            elif component[var1] > component[var0]:
                higher_component = component[var1]
                lower_component = component[var0]
                hc_var_set = vars_in_component[higher_component]
                expected_value = variable_values[var0] / values[i]
                actual_value = variable_values[var1]
                collapsefactor = expected_value / actual_value
                while len(hc_var_set)>0:
                    var_to_collapse = hc_var_set.pop()
                    variable_values[var_to_collapse] = variable_values[var_to_collapse] * collapsefactor
                    component[var_to_collapse] = lower_component
                vars_in_component.pop(higher_component)
        
        output = []
        for query in queries:
            if query[0] in variable_values and query[1] in variable_values:
                if component[query[0]] != component[query[1]]:
                    output.append(-1.0)
                    continue
                output.append( variable_values[query[0]] / variable_values[query[1]] )
            else:
                output.append(-1.0)
        return output

        


                
                    
                    

                


        