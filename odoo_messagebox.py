# -*- coding: utf-8 -*-
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
from openerp.osv import osv,fields
from openerp.tools.translate import _
import logging

_logger=logging.getLogger(__name__)


cb_ctx={
        #'name': _(u' '),
        'view_type': 'form',
        'view_mode': 'form',
        #'view_id': [res_id],
        'res_model': 'common.messagebox',
        'context': {'cb_function':'callback_test','msg_text':u'test message?'},
        'type': 'ir.actions.act_window',
        'nodestroy': True,
        'target': 'new',
        }

class odoo_messagebox(osv.osv):
    _name='odoo.messagebox'
    _description='test'
    _columns={
            'test':fields.char(u'Test',size=20),
            }

    def cb_test(self,cr,uid,ids,context=None):  #example function
        _logger.info(' ************ TEST  ******************')
        return True

 
    def action_test(self,cr,uid,ids,context=None):
         res = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'odoo_messagebox', 'common_messagebox_form')
         res_id = res and res[1] or False
         cb_ctx['name']= u'test messagebox'  #display  title
         cb_ctx['view_id']=[res_id]
         cb_ctx['context']['cb_function']='cb_test'   #This is you define function. 
         cb_ctx['context']['msg_text']=u'Are you sure?'  #display message 
         return cb_ctx

    def cb_test2(self,cr,uid,ids,context=None):  #example function
        _logger.info(' ************ TEST  222 ******************')
        return True

 
    def action_test_2(self,cr,uid,ids,context=None):
         res = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'odoo_messagebox', 'common_messagebox_form')
         res_id = res and res[1] or False
         cb_ctx['name']= u'test messagebox22'  #display  title
         cb_ctx['view_id']=[res_id]
         cb_ctx['context']['cb_function']='cb_test2'   #This is you define function. 
         cb_ctx['context']['msg_text']=u'Are you sure22?'  #display message 
         return cb_ctx
         
