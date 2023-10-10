/**
 * @id codeql/custom-queries/redundant_if_statement
 * @name If-else empty blocks present
 * @description Find empty block statements
 * @kind problem
 * @tags empty
 */

import csharp

from BlockStmt blk
where blk.isEmpty()
select blk, "This 'if' statement is redundant."
