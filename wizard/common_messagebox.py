#  -*- coding:utf-8  -*-
# __author__ =  xtjie@126.com
##############################################################################
#
#    website: http://www.oofittings.com http://www.kanyiyi.com http://www.cangzhou.pub
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv   import  fields,osv
from openerp.tools.translate  import _
class common_messagebox(osv.osv_memory):
    _name='common.messagebox'
    _description='common messagebox'
    
    def fields_view_get(self, cr, uid, view_id=None, view_type='form', toolbar=False,submenu=False, context=None):
         res = super(common_messagebox, self).fields_view_get(cr, uid, view_id, view_type, context, toolbar,submenu)
         res['arch'] = u"""
                 <form string="dummy">
                     <p><h3>%s</h3></p>
                    <footer>
                        <button name="do_action" string="OK"  type="object"
                            class="oe_highlight" />
                       <span style="margin-left:30px;">
                        <button special="cancel" string="Cancel"
                            class="oe_highlight" />
                       </span>     
                    </footer>
                </form>
                """%(context['msg_text'],)
         return res


    def do_action(self,cr,uid,ids,context=None):
        active_model=context.get('active_model')
        active_obj=self.pool.get(active_model)
        cbfuc=context.get('cb_function')
        exefunc=getattr(active_obj,cbfuc)
        return  exefunc(cr,uid,ids,context=context)
