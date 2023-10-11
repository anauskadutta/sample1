/**
 * @id csharp/custom-queries/unused-local-variable
 * @name Unused local variable
 * @description Finds local variables that are not accessed.
 * @kind problem
 * @tags variable
 *       local
 *       access
 */

import csharp

from LocalVariable v
where not exists(v.getAnAccess())
select v, "This local variable is not used."
