/**
 * @id csharp/custom-queries/unused-variable
 * @name Unused variable
 * @description Finds variables that are not used.
 * @kind problem
 * @tags variable
 *       unused
 */

import csharp

from Variable v
where not exists(v.getAnAssignedValue())
select v, "This variable is not used."
