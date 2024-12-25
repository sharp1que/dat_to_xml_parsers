// Generated from ./UnrealScript.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link UnrealScriptParser}.
 */
public interface UnrealScriptListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(UnrealScriptParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(UnrealScriptParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#classdecl}.
	 * @param ctx the parse tree
	 */
	void enterClassdecl(UnrealScriptParser.ClassdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#classdecl}.
	 * @param ctx the parse tree
	 */
	void exitClassdecl(UnrealScriptParser.ClassdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#classparams}.
	 * @param ctx the parse tree
	 */
	void enterClassparams(UnrealScriptParser.ClassparamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#classparams}.
	 * @param ctx the parse tree
	 */
	void exitClassparams(UnrealScriptParser.ClassparamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#constclassparams}.
	 * @param ctx the parse tree
	 */
	void enterConstclassparams(UnrealScriptParser.ConstclassparamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#constclassparams}.
	 * @param ctx the parse tree
	 */
	void exitConstclassparams(UnrealScriptParser.ConstclassparamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(UnrealScriptParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(UnrealScriptParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#packageidentifier}.
	 * @param ctx the parse tree
	 */
	void enterPackageidentifier(UnrealScriptParser.PackageidentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#packageidentifier}.
	 * @param ctx the parse tree
	 */
	void exitPackageidentifier(UnrealScriptParser.PackageidentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#declarations}.
	 * @param ctx the parse tree
	 */
	void enterDeclarations(UnrealScriptParser.DeclarationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#declarations}.
	 * @param ctx the parse tree
	 */
	void exitDeclarations(UnrealScriptParser.DeclarationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#constdecl}.
	 * @param ctx the parse tree
	 */
	void enterConstdecl(UnrealScriptParser.ConstdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#constdecl}.
	 * @param ctx the parse tree
	 */
	void exitConstdecl(UnrealScriptParser.ConstdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#constvalue}.
	 * @param ctx the parse tree
	 */
	void enterConstvalue(UnrealScriptParser.ConstvalueContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#constvalue}.
	 * @param ctx the parse tree
	 */
	void exitConstvalue(UnrealScriptParser.ConstvalueContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#classval}.
	 * @param ctx the parse tree
	 */
	void enterClassval(UnrealScriptParser.ClassvalContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#classval}.
	 * @param ctx the parse tree
	 */
	void exitClassval(UnrealScriptParser.ClassvalContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#objectval}.
	 * @param ctx the parse tree
	 */
	void enterObjectval(UnrealScriptParser.ObjectvalContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#objectval}.
	 * @param ctx the parse tree
	 */
	void exitObjectval(UnrealScriptParser.ObjectvalContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#vardecl}.
	 * @param ctx the parse tree
	 */
	void enterVardecl(UnrealScriptParser.VardeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#vardecl}.
	 * @param ctx the parse tree
	 */
	void exitVardecl(UnrealScriptParser.VardeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#arrayindex}.
	 * @param ctx the parse tree
	 */
	void enterArrayindex(UnrealScriptParser.ArrayindexContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#arrayindex}.
	 * @param ctx the parse tree
	 */
	void exitArrayindex(UnrealScriptParser.ArrayindexContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#varparams}.
	 * @param ctx the parse tree
	 */
	void enterVarparams(UnrealScriptParser.VarparamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#varparams}.
	 * @param ctx the parse tree
	 */
	void exitVarparams(UnrealScriptParser.VarparamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#configgroup}.
	 * @param ctx the parse tree
	 */
	void enterConfiggroup(UnrealScriptParser.ConfiggroupContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#configgroup}.
	 * @param ctx the parse tree
	 */
	void exitConfiggroup(UnrealScriptParser.ConfiggroupContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#vartype}.
	 * @param ctx the parse tree
	 */
	void enterVartype(UnrealScriptParser.VartypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#vartype}.
	 * @param ctx the parse tree
	 */
	void exitVartype(UnrealScriptParser.VartypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#basictype}.
	 * @param ctx the parse tree
	 */
	void enterBasictype(UnrealScriptParser.BasictypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#basictype}.
	 * @param ctx the parse tree
	 */
	void exitBasictype(UnrealScriptParser.BasictypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#varidentifier}.
	 * @param ctx the parse tree
	 */
	void enterVaridentifier(UnrealScriptParser.VaridentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#varidentifier}.
	 * @param ctx the parse tree
	 */
	void exitVaridentifier(UnrealScriptParser.VaridentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#arraydecl}.
	 * @param ctx the parse tree
	 */
	void enterArraydecl(UnrealScriptParser.ArraydeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#arraydecl}.
	 * @param ctx the parse tree
	 */
	void exitArraydecl(UnrealScriptParser.ArraydeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#dynarraydecl}.
	 * @param ctx the parse tree
	 */
	void enterDynarraydecl(UnrealScriptParser.DynarraydeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#dynarraydecl}.
	 * @param ctx the parse tree
	 */
	void exitDynarraydecl(UnrealScriptParser.DynarraydeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#classtype}.
	 * @param ctx the parse tree
	 */
	void enterClasstype(UnrealScriptParser.ClasstypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#classtype}.
	 * @param ctx the parse tree
	 */
	void exitClasstype(UnrealScriptParser.ClasstypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#enumdecl}.
	 * @param ctx the parse tree
	 */
	void enterEnumdecl(UnrealScriptParser.EnumdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#enumdecl}.
	 * @param ctx the parse tree
	 */
	void exitEnumdecl(UnrealScriptParser.EnumdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#enumoptions}.
	 * @param ctx the parse tree
	 */
	void enterEnumoptions(UnrealScriptParser.EnumoptionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#enumoptions}.
	 * @param ctx the parse tree
	 */
	void exitEnumoptions(UnrealScriptParser.EnumoptionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#structdecl}.
	 * @param ctx the parse tree
	 */
	void enterStructdecl(UnrealScriptParser.StructdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#structdecl}.
	 * @param ctx the parse tree
	 */
	void exitStructdecl(UnrealScriptParser.StructdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#structparams}.
	 * @param ctx the parse tree
	 */
	void enterStructparams(UnrealScriptParser.StructparamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#structparams}.
	 * @param ctx the parse tree
	 */
	void exitStructparams(UnrealScriptParser.StructparamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#structbody}.
	 * @param ctx the parse tree
	 */
	void enterStructbody(UnrealScriptParser.StructbodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#structbody}.
	 * @param ctx the parse tree
	 */
	void exitStructbody(UnrealScriptParser.StructbodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#replicationblock}.
	 * @param ctx the parse tree
	 */
	void enterReplicationblock(UnrealScriptParser.ReplicationblockContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#replicationblock}.
	 * @param ctx the parse tree
	 */
	void exitReplicationblock(UnrealScriptParser.ReplicationblockContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#replicationbody}.
	 * @param ctx the parse tree
	 */
	void enterReplicationbody(UnrealScriptParser.ReplicationbodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#replicationbody}.
	 * @param ctx the parse tree
	 */
	void exitReplicationbody(UnrealScriptParser.ReplicationbodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(UnrealScriptParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(UnrealScriptParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#statedecl}.
	 * @param ctx the parse tree
	 */
	void enterStatedecl(UnrealScriptParser.StatedeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#statedecl}.
	 * @param ctx the parse tree
	 */
	void exitStatedecl(UnrealScriptParser.StatedeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#statebody}.
	 * @param ctx the parse tree
	 */
	void enterStatebody(UnrealScriptParser.StatebodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#statebody}.
	 * @param ctx the parse tree
	 */
	void exitStatebody(UnrealScriptParser.StatebodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#stateignore}.
	 * @param ctx the parse tree
	 */
	void enterStateignore(UnrealScriptParser.StateignoreContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#stateignore}.
	 * @param ctx the parse tree
	 */
	void exitStateignore(UnrealScriptParser.StateignoreContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#statelabels}.
	 * @param ctx the parse tree
	 */
	void enterStatelabels(UnrealScriptParser.StatelabelsContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#statelabels}.
	 * @param ctx the parse tree
	 */
	void exitStatelabels(UnrealScriptParser.StatelabelsContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#stateparams}.
	 * @param ctx the parse tree
	 */
	void enterStateparams(UnrealScriptParser.StateparamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#stateparams}.
	 * @param ctx the parse tree
	 */
	void exitStateparams(UnrealScriptParser.StateparamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#functiondecl}.
	 * @param ctx the parse tree
	 */
	void enterFunctiondecl(UnrealScriptParser.FunctiondeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#functiondecl}.
	 * @param ctx the parse tree
	 */
	void exitFunctiondecl(UnrealScriptParser.FunctiondeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#normalfunc}.
	 * @param ctx the parse tree
	 */
	void enterNormalfunc(UnrealScriptParser.NormalfuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#normalfunc}.
	 * @param ctx the parse tree
	 */
	void exitNormalfunc(UnrealScriptParser.NormalfuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#functiontype}.
	 * @param ctx the parse tree
	 */
	void enterFunctiontype(UnrealScriptParser.FunctiontypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#functiontype}.
	 * @param ctx the parse tree
	 */
	void exitFunctiontype(UnrealScriptParser.FunctiontypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#functionparams}.
	 * @param ctx the parse tree
	 */
	void enterFunctionparams(UnrealScriptParser.FunctionparamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#functionparams}.
	 * @param ctx the parse tree
	 */
	void exitFunctionparams(UnrealScriptParser.FunctionparamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#constfuncparams}.
	 * @param ctx the parse tree
	 */
	void enterConstfuncparams(UnrealScriptParser.ConstfuncparamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#constfuncparams}.
	 * @param ctx the parse tree
	 */
	void exitConstfuncparams(UnrealScriptParser.ConstfuncparamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#operatorfunc}.
	 * @param ctx the parse tree
	 */
	void enterOperatorfunc(UnrealScriptParser.OperatorfuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#operatorfunc}.
	 * @param ctx the parse tree
	 */
	void exitOperatorfunc(UnrealScriptParser.OperatorfuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#operatortype}.
	 * @param ctx the parse tree
	 */
	void enterOperatortype(UnrealScriptParser.OperatortypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#operatortype}.
	 * @param ctx the parse tree
	 */
	void exitOperatortype(UnrealScriptParser.OperatortypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#binaryoperator}.
	 * @param ctx the parse tree
	 */
	void enterBinaryoperator(UnrealScriptParser.BinaryoperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#binaryoperator}.
	 * @param ctx the parse tree
	 */
	void exitBinaryoperator(UnrealScriptParser.BinaryoperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#unaryoperator}.
	 * @param ctx the parse tree
	 */
	void enterUnaryoperator(UnrealScriptParser.UnaryoperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#unaryoperator}.
	 * @param ctx the parse tree
	 */
	void exitUnaryoperator(UnrealScriptParser.UnaryoperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#opidentifier}.
	 * @param ctx the parse tree
	 */
	void enterOpidentifier(UnrealScriptParser.OpidentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#opidentifier}.
	 * @param ctx the parse tree
	 */
	void exitOpidentifier(UnrealScriptParser.OpidentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#operatornames}.
	 * @param ctx the parse tree
	 */
	void enterOperatornames(UnrealScriptParser.OperatornamesContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#operatornames}.
	 * @param ctx the parse tree
	 */
	void exitOperatornames(UnrealScriptParser.OperatornamesContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#functionargs}.
	 * @param ctx the parse tree
	 */
	void enterFunctionargs(UnrealScriptParser.FunctionargsContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#functionargs}.
	 * @param ctx the parse tree
	 */
	void exitFunctionargs(UnrealScriptParser.FunctionargsContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#functionargtype}.
	 * @param ctx the parse tree
	 */
	void enterFunctionargtype(UnrealScriptParser.FunctionargtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#functionargtype}.
	 * @param ctx the parse tree
	 */
	void exitFunctionargtype(UnrealScriptParser.FunctionargtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#functionbody}.
	 * @param ctx the parse tree
	 */
	void enterFunctionbody(UnrealScriptParser.FunctionbodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#functionbody}.
	 * @param ctx the parse tree
	 */
	void exitFunctionbody(UnrealScriptParser.FunctionbodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#localdecl}.
	 * @param ctx the parse tree
	 */
	void enterLocaldecl(UnrealScriptParser.LocaldeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#localdecl}.
	 * @param ctx the parse tree
	 */
	void exitLocaldecl(UnrealScriptParser.LocaldeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#localtype}.
	 * @param ctx the parse tree
	 */
	void enterLocaltype(UnrealScriptParser.LocaltypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#localtype}.
	 * @param ctx the parse tree
	 */
	void exitLocaltype(UnrealScriptParser.LocaltypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#codeblock}.
	 * @param ctx the parse tree
	 */
	void enterCodeblock(UnrealScriptParser.CodeblockContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#codeblock}.
	 * @param ctx the parse tree
	 */
	void exitCodeblock(UnrealScriptParser.CodeblockContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(UnrealScriptParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(UnrealScriptParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#assertion}.
	 * @param ctx the parse tree
	 */
	void enterAssertion(UnrealScriptParser.AssertionContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#assertion}.
	 * @param ctx the parse tree
	 */
	void exitAssertion(UnrealScriptParser.AssertionContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#ifstatement}.
	 * @param ctx the parse tree
	 */
	void enterIfstatement(UnrealScriptParser.IfstatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#ifstatement}.
	 * @param ctx the parse tree
	 */
	void exitIfstatement(UnrealScriptParser.IfstatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#switchstatement}.
	 * @param ctx the parse tree
	 */
	void enterSwitchstatement(UnrealScriptParser.SwitchstatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#switchstatement}.
	 * @param ctx the parse tree
	 */
	void exitSwitchstatement(UnrealScriptParser.SwitchstatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#whileloop}.
	 * @param ctx the parse tree
	 */
	void enterWhileloop(UnrealScriptParser.WhileloopContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#whileloop}.
	 * @param ctx the parse tree
	 */
	void exitWhileloop(UnrealScriptParser.WhileloopContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#doloop}.
	 * @param ctx the parse tree
	 */
	void enterDoloop(UnrealScriptParser.DoloopContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#doloop}.
	 * @param ctx the parse tree
	 */
	void exitDoloop(UnrealScriptParser.DoloopContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#foreachloop}.
	 * @param ctx the parse tree
	 */
	void enterForeachloop(UnrealScriptParser.ForeachloopContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#foreachloop}.
	 * @param ctx the parse tree
	 */
	void exitForeachloop(UnrealScriptParser.ForeachloopContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#forloop}.
	 * @param ctx the parse tree
	 */
	void enterForloop(UnrealScriptParser.ForloopContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#forloop}.
	 * @param ctx the parse tree
	 */
	void exitForloop(UnrealScriptParser.ForloopContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#returnstatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnstatement(UnrealScriptParser.ReturnstatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#returnstatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnstatement(UnrealScriptParser.ReturnstatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#caserule}.
	 * @param ctx the parse tree
	 */
	void enterCaserule(UnrealScriptParser.CaseruleContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#caserule}.
	 * @param ctx the parse tree
	 */
	void exitCaserule(UnrealScriptParser.CaseruleContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#casecodeblock}.
	 * @param ctx the parse tree
	 */
	void enterCasecodeblock(UnrealScriptParser.CasecodeblockContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#casecodeblock}.
	 * @param ctx the parse tree
	 */
	void exitCasecodeblock(UnrealScriptParser.CasecodeblockContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#defaultrule}.
	 * @param ctx the parse tree
	 */
	void enterDefaultrule(UnrealScriptParser.DefaultruleContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#defaultrule}.
	 * @param ctx the parse tree
	 */
	void exitDefaultrule(UnrealScriptParser.DefaultruleContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(UnrealScriptParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(UnrealScriptParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(UnrealScriptParser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(UnrealScriptParser.PrimaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#creator}.
	 * @param ctx the parse tree
	 */
	void enterCreator(UnrealScriptParser.CreatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#creator}.
	 * @param ctx the parse tree
	 */
	void exitCreator(UnrealScriptParser.CreatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#parExpression}.
	 * @param ctx the parse tree
	 */
	void enterParExpression(UnrealScriptParser.ParExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#parExpression}.
	 * @param ctx the parse tree
	 */
	void exitParExpression(UnrealScriptParser.ParExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#expressionList}.
	 * @param ctx the parse tree
	 */
	void enterExpressionList(UnrealScriptParser.ExpressionListContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#expressionList}.
	 * @param ctx the parse tree
	 */
	void exitExpressionList(UnrealScriptParser.ExpressionListContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#defaultpropertiesblock}.
	 * @param ctx the parse tree
	 */
	void enterDefaultpropertiesblock(UnrealScriptParser.DefaultpropertiesblockContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#defaultpropertiesblock}.
	 * @param ctx the parse tree
	 */
	void exitDefaultpropertiesblock(UnrealScriptParser.DefaultpropertiesblockContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#defprop}.
	 * @param ctx the parse tree
	 */
	void enterDefprop(UnrealScriptParser.DefpropContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#defprop}.
	 * @param ctx the parse tree
	 */
	void exitDefprop(UnrealScriptParser.DefpropContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#defpropidentifier}.
	 * @param ctx the parse tree
	 */
	void enterDefpropidentifier(UnrealScriptParser.DefpropidentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#defpropidentifier}.
	 * @param ctx the parse tree
	 */
	void exitDefpropidentifier(UnrealScriptParser.DefpropidentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#qualifiedidentifier}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedidentifier(UnrealScriptParser.QualifiedidentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#qualifiedidentifier}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedidentifier(UnrealScriptParser.QualifiedidentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link UnrealScriptParser#identifierlist}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierlist(UnrealScriptParser.IdentifierlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link UnrealScriptParser#identifierlist}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierlist(UnrealScriptParser.IdentifierlistContext ctx);
}